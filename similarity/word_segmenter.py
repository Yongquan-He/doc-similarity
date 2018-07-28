'''
按照段落进行分词
@:param  artical_generator
@:param  stop_word_path
by: Junyi
'''
import jieba as jb
import redis

# TODO 实现save_to_redis(部署时)将分词的结果保存至redis数据库

class WordSegmenter(object):

    def __init__(self, stop_word_path="stopWords.txt"):
        self.stop_word_path = stop_word_path
        self.stop_word_list = self.get_stop_word_list(self.stop_word_path)
        self.extend_word_list = [' ', '\xa0', '\n', '\t']    # 一些无法列在stopWords.txt中的停用词

    def get_stop_word_list(self, stop_word_path):
        stop_word_list = [line.strip() for line in open(self.stop_word_path, encoding='UTF-8').readlines()]
        return stop_word_list

    def separate_text(self, text):
        text_seperated = jb.lcut(text)
        return [word for word in text_seperated if word not in self.extend_word_list]

    def filter_stop_word(self, text):
        text_ = [word for word in text if word not in self.stop_word_list]
        return text_

    def separate_artical_for_calculate(self, artical_generator, filter_stop_word=True):
        artical_separated = []
        for paragraph in artical_generator:
            text_separated = self.separate_text(paragraph)
            if filter_stop_word:
                text_separated= self.filter_stop_word(text_separated)
            if text_separated:
                artical_separated.extend(text_separated)
        return artical_separated

    # 将分词后的列表保存至redis数据库
    def save_to_redis(self):
        pass

    def read_from_redis_for_calculate(self):
        pass