# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_fwMNXxRr885lI2trO3CHMrfKtuoP1_N
"""



file1 = "history is the study of systematic study of the past"
file2 = "history is the study systematic study of the past this is just for study"
def jaccard_similarity(text1,text2):
  set1 = set(text1.split())
  set2 = set (text2.split())
  intersection = set1.intersection(set2)
  union = set1.union(set2)
  similarity = len(intersection) / len(union)
  return similarity, intersection

  similarity, common_words = jaccard_similarity(file1,file2)
  print(f"similarity: {similarity:.2f}")
  print(f"common_words: {common_words}")