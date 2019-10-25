import scipy
from scipy import stats

list1 = [1,2,3,4,5]  
list2 = [6,7,8,9,0]
#For example, to calculate the correlation coefficient between list1 and list2
print(" Pearson correlation coefficient: ", stats.pearsonr(list1,list2))
print(" Spearman's rank correlation coefficient: ", stats.spearmanr(list1,list2))

