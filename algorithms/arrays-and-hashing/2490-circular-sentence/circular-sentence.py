class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_list = sentence.split()
        
        for i in range(len(sentence_list) + 1):
            if i + 1 < len(sentence_list):
                if sentence_list[i][-1] != sentence_list[i + 1][0]:
                    return False
            else:
                if sentence_list[int(i %(len(sentence_list)))][0] != sentence_list[i-1][-1]:
                    return False
        return True