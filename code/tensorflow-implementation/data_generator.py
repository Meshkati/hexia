import cv2
import numpy as np
from utils import get_image_id, clean_sentence, confidence_to_one_hot
import json
import os

# from text_generator import TextGenerator

class DataGenerator:

    def __init__(self, image_path, q_path, a_path, image_rescale, image_horizontal_flip, image_target_size):
        self.image_path = image_path
        self.q_path = q_path
        self.a_path = a_path
        self.image_rescale = image_rescale
        self.image_horizontal_flip = image_horizontal_flip
        self.image_target_size = image_target_size

        # Load Questions and Answers JSON into memory
        self.load_qa_into_mem()

    def load_qa_into_mem(self):
        """
        Load json files to memory for further usage.
        """
        # Load all image files of directory into the memory
        self.image_list = os.listdir(self.image_path)

        with open(self.q_path, encoding='utf-8') as q_file:
            self.q_data = json.loads(q_file.read())

        with open(self.a_path, encoding='utf-8') as a_file:
            self.a_data = json.loads(a_file.read())

    def mini_batch_generator(self):
        """
        Generator for feeding data through Tensorflow dataset API.
        """

        # Generate a batch of images
        # for each image in the batch generate

        # For each file in the image list
        for image_name in self.image_list:

            # Read image from directory
            img = cv2.imread(os.path.join(self.image_path, image_name))
            img = cv2.resize(img, (64, 64))

            # Normalize
            img = img / 255.0

            # Extract the image ID
            img_id = get_image_id(image_name)

            # Extract questions, answers, and labels (confidences) from the JSON files
            for question in self.q_data['questions']:
                if(question['image_id'] == int(img_id)):
                    for annotation in self.a_data['annotations']:
                        if(annotation['question_id'] == question['question_id']):
                            answer_no = 0
                            for _ in annotation['answers']:

                                batch_item = {}
                                batch_item['image'] = img
                                batch_item['sentence'] = clean_sentence(question['question'] + ' ' + annotation['answers'][answer_no]['answer'])
                                # batch_item['question'] = clean_sentence(question['question'])
                                # batch_item['answer'] = clean_sentence(annotation['answers'][answer_no]['answer'])
                                batch_item['iqa_label'] = confidence_to_one_hot(annotation['answers'][answer_no]['answer_confidence'])
                                answer_no = answer_no + 1
                                # print(len(batch_item['sentence']))
                                # print(len(batch_item['sentence'].split()))
                                yield np.array(batch_item['image'].flatten()), batch_item['sentence'], np.array(batch_item['iqa_label'])