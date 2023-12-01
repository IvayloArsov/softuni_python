from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def __get_category(self, id):
        return [category for category in self.categories if id == category.id][0]

    def __get_topic(self, id):
        return [topic for topic in self.topics if id == topic.id][0]

    def __get_document(self, id):
        return [document for document in self.documents if id == document.id][0]

    def edit_category(self, category_id: int, new_name: str):
        find_category = self.__get_category(category_id)
        find_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        find_topic = self.__get_topic(topic_id)
        find_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        find_document = self.__get_document(document_id)
        find_document.edit(new_file_name)

    def delete_category(self, category_id):
        find_category = self.__get_category(category_id)
        if find_category in self.categories:
            self.categories.remove(find_category)

    def delete_topic(self, topic_id):
        find_topic = self.__get_topic(topic_id)
        if find_topic in self.topics:
            self.topics.remove(find_topic)

    def delete_document(self, document_id):
        find_doc = self.__get_document(document_id)
        if find_doc in self.documents:
            self.documents.remove(find_doc)

    def get_document(self, document_id):
        find_doc = self.__get_document(document_id)
        return find_doc

    def __repr__(self):
        document_strings = []
        for doc in self.documents:
            document_strings.append(str(doc))
        return '\n'.join(document_strings)
