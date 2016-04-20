class QAConcept(object):
    """
    A QAConcept represents a group of QAPair variations asking about the same fact-based concept.
    """

    def __init__(self):
        self.qa_pair_variations = []

    def new_qa_pair(self, question, answer, context_map):
        """
        returns a new QA pair associated with the current QA concept
        """
        qa_pair = QAPair(self, question, answer, context_map)
        self.qa_pair_variations.append(qa_pair)
        return qa_pair


class EntityClassLevelQA(QAConcept):
    def __init__(self, entity_class):
        super(EntityClassLevelQA, self).__init__()
        self.entity_class = entity_class


class EntityInstanceSelfQA(QAConcept):
    def __init__(self, entity_instance):
        super(EntityInstanceSelfQA, self).__init__()
        self.entity_instance = entity_instance


class EntityPropertyQA(QAConcept):
    def __init__(self, entity_instance, property_def):
        super(EntityPropertyQA, self).__init__()
        self.entity_instance = entity_instance
        self.property_def = property_def


class EntityRelationQA(QAConcept):
    def __init__(self, entity_instance, relation_def):
        super(EntityRelationQA, self).__init__()
        self.entity_instance = entity_instance
        self.relation_deff = relation_def


class QAPair(object):
    """
    A specific variation of QA pair
    """

    def __init__(self, qa_concept, question, answer, context_map):
        """
        :param qa_concept: the parent QA concept associated with this QA pair.
        :param question:
        :param answer:
        :param context_map: {entity_class_name: entity_instance_id}
        :return:
        """
        self.qa_concept = qa_concept
        self.question = question
        self.answer = answer
        self.context_map = context_map
        self.qa_pairs_with_matching_score = [{
            'question': question,
            'answer': answer,
            'score': 100
        }]

    def __repr__(self):
        return 'Q: %s, A: %s' % (self.question, self.answer)

    def add_qa_pair_with_matching_score(self, question, answer, score):
        """
        used for generating training label
        :param score: 0~100
        """
        self.qa_pairs_with_matching_score.append({
            'question': question,
            'answer': answer,
            'score': score
        })

    def to_json_dict(self, is_for_training=False):
        result = {
            'question': self.question,
            'answer': self.answer,
            'context': self.context_map,
        }
        if is_for_training:
            result.update({
                'question_topic_words': [],
                'answer_topic_words': [],
                'qa_pairs_with_matching_score': self.qa_pairs_with_matching_score
            })
        return result

