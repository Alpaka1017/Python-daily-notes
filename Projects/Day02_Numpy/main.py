import numpy as np

### 1. NumPy入门
# 版本
def np_version():
    print(np.__version__)


def np_array_dims():
    # 0-D
    arr_0d = np.array(63)
    # print('0-D array example/ scalar:', arr_0d)
    # 1-D
    arr_1d = np.array([1, 2, 3, 4, 5, 6])
    # print('1-D array example:', arr_1d)
    # 2-D：其元素为一维数组
    arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    # print('2-D array example:', arr_2d)
    # 3-D：其元素为二维数组
    arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    # print('3-D array example:', arr_3d)
    return arr_0d, arr_1d, arr_2d, arr_3d


def np_array_ndim(*arrs):
    for arr in arrs:
        if isinstance(arr, np.ndarray):
            print('Dimension of the array:', arr.ndim)
        else:
            return -1
    # raise ValueError('No np.ndarray type arguments found!')


def np_array_multi_dim(dim):
    arr_multi = np.array([1, 2, 3, 4], ndmin=dim)
    return arr_multi


def np_array_index():
    arr_1 = np.array([1, 2, 3, 4, 5])
    print('Summation of elements of a 1-D array: %d + %d = %d' % (arr_1[0], arr_1[3], arr_1[0] + arr_1[3]))
    print(f'Summation: {arr_1[0]} + {arr_1[3]} = {arr_1[0] + arr_1[3]}')

    arr_2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(f'3nd element on the 2nd dim: {arr_2[1, 2]}')

    arr_3 = np.array([[[1, 2, 3], [4, 5, 6]],
                      [[7, 8, 9], [10, 11, 12]]])
    print(f'3rd element of 2nd array of 2nd array of the 3-D array: {arr_3[1, 1, 2]}')

    arr_neg = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print('Last element from 2nd dim: ', arr_neg[1, -1])


def np_array_slice():
    arr_1_slice = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr_1_slice[1:5])

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    # 提取第1和2个向量的第5个元素
    print(arr[0:2, 2:3])


def np_array_advanced():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # 将数组逆时针旋转90度
    arr_rotated = np.rot90(arr)
    print("rotated array:\n", arr_rotated)

    # 沿着水平方向翻转数组
    arr_flipped_lr = np.fliplr(arr)
    print("flipped lr array:\n", arr_flipped_lr)

    # 沿着垂直方向翻转数组
    arr_flipped_ud = np.flipud(arr)
    print("flipped ud array:\n", arr_flipped_ud)

    # 沿着第二个轴翻转数组
    arr_flipped_axis = np.flip(arr, axis=1)
    print("flipped axis array:\n", arr_flipped_axis)


def np_array_concantenate():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    arr = np.concatenate((arr1, arr2), axis=0)
    arr_stack_row = np.stack((arr1, arr2), axis=0)  # 1st dim：按行连接，连接的是列
    arr_stack_col = np.stack((arr1, arr2), axis=1)  # 2nd dim：按列连接，连接的是行

    arr_hstack = np.hstack((arr1, arr2))
    arr_vstack = np.vstack((arr1, arr2))
    arr_dstack = np.dstack((arr1, arr2))

    print(f'Concatenate axis = 0: {arr}')
    print(f'"np.hstack" function: {arr_hstack}')

    print(f'Concatenate along row (axis = 0): {arr_stack_row}')
    print(f'"np.vstack" function: {arr_vstack}')

    print(f'Concatenate along column (axis = 1): {arr_stack_col}')
    print(f'"np.dstack()" function: {arr_dstack}')


def np_array_split():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

    newarr_row = np.array_split(arr, 3, axis=0)  # 二维数组沿1st dim.拆分（按行）
    newarr_col = np.array_split(arr, 3, axis=1)  # 二维数组沿2nd dim.拆分（按列）
    newarr_hsplit = np.hsplit(arr, 3)
    newarr_vsplit = np.vsplit(arr, 3)
    # newarr_dsplit = np.dsplit(arr, 3)

    print(f'Split 1. dim:\n {newarr_row}')  # 1st dim.，按行拆分 = vsplit()
    print(f'Split with "vsplit()":\n {newarr_vsplit}')
    print(f'Split 2. dim:\n {newarr_col}')  # 2nd dim., 按列拆分 = hsplit()
    print(f'Split with "vsplit()":\n {newarr_hsplit}')


def np_array_search():
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    arr_search = np.where(arr == 4)

    # arr_search为元组对象，arr_search[0]为返回的索引列表（类型为np.ndarray），arr_search[0][2]可以访问第3个索引对象
    print(
        f'返回索引：{arr_search}\n数据类型为：{type(arr_search)}\n索引数组{arr_search[0]}的类型为：{type(arr_search[0])}\n其中第3个满足搜索的索引值为：{arr_search[0][2]}\n')

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    idx_left = np.searchsorted(arr, 7.5)
    idx_right = np.searchsorted(arr, 7.1, side='right')

    print(idx_left)
    print(idx_right)

    arr = np.array([1, 3, 5, 7])
    x = np.searchsorted(arr, [2, 4, 6])
    print(x)


def np_array_filter(ndArray_filter):
    # 作用，对数组中的元素进行遍历，值>60的返回True，否则则返回False
    filter_list = []
    ndArray_float = ndArray_filter.astype('float')
    for element in ndArray_float:
        if element >= 60:
            filter_list.append(True)
        else:
            filter_list.append(False)
    return filter_list


if __name__ == '__main__':
    # 1. 版本
    # np_version()

    # 2. ndim方法获取数组维数
    arr_0d, arr_1d, arr_2d, arr_3d = np_array_dims()
    # np_array_ndim(*np_array_dims())

    # 3. 创建多维数组
    '''dim = input('Input the expected dim of array:')
    array_multi = np_array_multi_dim(int(dim))
    print(array_multi)
    print('Dimension:', array_multi.ndim)'''

    # 4. 数组的索引
    # np_array_index()

    # 5. 数组的切片
    # np_array_slice()

    # 6. 数组变换的高级操作
    # np_array_advanced()

    # 7. 数组的连接操作
    # np_array_concantenate()

    # 8. 数组的拆分
    # np_array_split()

    # 9. 数组的搜索和排序
    # np_array_search()

    # 10. 数组过滤
    '''arr = np.array([1, 5, 3, 87, 687, 2, 4, '4', '456', 6, '64'])
    newarr = arr[np_array_filter(arr)]
    print(newarr)'''
    from numpy import random

    x = [1, 2, 3, 4]
    y = [4, 5, 6, 7]
    z = []

    for i, j in zip(x, y):
        z.append(i + j)
    print(z)
