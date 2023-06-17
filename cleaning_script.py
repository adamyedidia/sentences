import pickle
import IPython

sentences = pickle.load(open('sentences.p', 'rb'))['sentences']


def append_or_create_new_array(dictionary, key, value):
    if key in dictionary.keys():
        dictionary[key] = dictionary[key]+[value,]

    else:
        dictionary[key] = [value, ]


# count number of objects
sentences_with_numbers_of_objects = {}
sentences_with_numbers_of_periods = {}
sentences_with_pairs_of_genders = {}
sentences_with_pairs_of_tested_genders = {}

tested_genders = ['male', 'female', 'none']


for sentence_dict in sentences:
    sentence = sentence_dict['sentence']
    subject_dict = sentence_dict['subject']
    object_list = sentence_dict['objects']

    num_objects = len(object_list)
    num_periods = sentence.count('.')

    if num_periods == 1 and num_objects == 1:
        subject_gender = subject_dict['gender']
        object_gender = object_list[0]['gender']
        if subject_gender in tested_genders and object_gender in tested_genders:
            append_or_create_new_array(
                sentences_with_pairs_of_tested_genders,
                (subject_gender, object_gender),
                sentence_dict
            )
        append_or_create_new_array(
            sentences_with_pairs_of_genders,
            (subject_gender, object_gender),
            sentence_dict
        )

    append_or_create_new_array(
        sentences_with_numbers_of_objects,
        num_objects,
        sentence_dict
    )
    append_or_create_new_array(
        sentences_with_numbers_of_periods,
        num_periods,
        sentence_dict
    )


IPython.embed()