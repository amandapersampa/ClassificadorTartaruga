import src.CGT.KFold_Validation as kf
from src.CGT.Error_Validate import save_lbp_RGB, save_lbp_YCBCR

# A primeira vez que rodar: b_update = True

def run(save=False, random=True, lbp='default', kfold_update=False):
    error_file, name_test, name_pred, result_file, result_name = kf.accuracyK_Fold_SVM_RGB(save=save, random=random,
                                                                                           lbp=lbp, b_update=True,
                                                                                           kfold_update=kfold_update)
    save_lbp_RGB(error_file, name_test, name_pred, 'SVM', 'RGB', 'erro', lbp=lbp)
    # save_lbp_RGB(result_file, result_name, result_name, 'SVM', 'RGB', 'acerto')

    error_file, name_test, name_pred, result_file, result_name = kf.accuracyK_Fold_SVM_YCBCR(save=save, random=random,
                                                                                             lbp=lbp,
                                                                                             kfold_update=kfold_update)
    save_lbp_YCBCR(error_file, name_test, name_pred, 'SVM', 'YCBCR', 'erro', lbp=lbp)
    # save_lbp_YCBCR(result_file, result_name, result_name, 'SVM', 'YCBCR', 'acerto')

    error_file, name_test, name_pred, result_file, result_name = kf.accuracyK_Fold_KNN_YCBCR(save=save, random=random,
                                                                                             lbp=lbp,
                                                                                             kfold_update=kfold_update)
    save_lbp_YCBCR(error_file, name_test, name_pred, 'KNN', 'YCBCR', 'erro', lbp=lbp)
    # save_lbp_YCBCR(result_file, result_name, result_name, 'KNN', 'YCBCR', 'acerto')

    error_file, name_test, name_pred, result_file, result_name = kf.accuracyK_Fold_KNN_RGB(save=save, random=random,
                                                                                           lbp=lbp,
                                                                                           kfold_update=kfold_update)
    save_lbp_RGB(error_file, name_test, name_pred, 'KNN', 'RGB', 'erro', lbp=lbp)
    # save_lbp_RGB(result_file, result_name, result_name, 'KNN', 'RGB','acerto')


# -------------------------------------------------------#

#kf.clean_Result()

'''
* 'default': original local binary pattern which is gray scale but not
    rotation invariant.
* 'ror': extension of default implementation which is gray scale and
    rotation invariant.
* 'uniform': improved rotation invariance with uniform patterns and
    finer quantization of the angular space which is gray scale and
    rotation invariant.
* 'nri_uniform': non rotation-invariant uniform patterns variant
    which is only gray scale invariant [2]_.
* 'var': rotation invariant variance measures of the contrast of local
    image texture which is rotation but not gray scale invariant.
'''
print('***************************************************************************************')
print('*************************************** default ***************************************')
print('***************************************************************************************')
run(lbp='default')

print('***************************************************************************************')
print('***************************************** ror *****************************************')
print('***************************************************************************************')
run(lbp='ror')

print('***************************************************************************************')
print('*************************************** uniform ***************************************')
print('***************************************************************************************')
run(lbp='uniform')

#print('***************************************************************************************')
#print('***************************************** var *****************************************')
#print('***************************************************************************************')
#run(lbp='var')
