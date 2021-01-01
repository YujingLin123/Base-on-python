DataFrame.to_csv(path_or_buf=None, sep=', ', na_rep='', float_format=None, columns=None, 
header=True, index=True, index_label=None, mode='w', encoding=None, compression=None, 
quoting=None, quotechar='"', line_terminator='\n', chunksize=None, tupleize_cols=None, 
date_format=None, doublequote=True, escapechar=None, decimal='.')


"""
path_or_buf=None： string or file handle, default None
File path or object, if None is provided the result is returned as a string.
字符串或文件句柄，默认无文件
路径或对象，如果没有提供，结果将返回为字符串。

sep : character, default ‘,’
Field delimiter for the output file.
默认字符 ‘ ，’
输出文件的字段分隔符。

na_rep : string, default ‘’
Missing data representation
字符串，默认为 ‘’
浮点数格式字符串

float_format : string, default None
Format string for floating point numbers
字符串，默认为 None
浮点数格式字符串

columns : sequence, optional Columns to write
顺序，可选列写入

header : boolean or list of string, default True
Write out the column names. If a list of strings is given it is assumed to be aliases for the column names
字符串或布尔列表，默认为true
写出列名。如果给定字符串列表，则假定为列名的别名。

index : boolean, default True
Write row names (index)
布尔值，默认为Ture
写入行名称（索引）

index_label : string or sequence, or False, default None
Column label for index column(s) if desired. If None is given, and header and index are True, then the index names are used. A sequence should be given if the DataFrame uses MultiIndex. If False do not print fields for index names. Use index_label=False for easier importing in R
字符串或序列，或False,默认为None
如果需要，可以使用索引列的列标签。如果没有给出，且标题和索引为True，则使用索引名称。如果数据文件使用多索引，则应该使用这个序列。如果值为False，不打印索引字段。在R中使用index_label=False 更容易导入索引.

mode : str
模式：值为‘str’，字符串
Python写模式，默认“w”

encoding : string, optional
编码：字符串，可选
表示在输出文件中使用的编码的字符串，Python 2上默认为“ASCII”和Python 3上默认为“UTF-8”。

compression : string, optional
字符串，可选项
表示在输出文件中使用的压缩的字符串，允许值为“gzip”、“bz2”、“xz”，仅在第一个参数是文件名时使用。

line_terminator : string, default ‘\n’
字符串，默认为 ‘\n’
在输出文件中使用的换行字符或字符序列

quoting : optional constant from csv module
CSV模块的可选常量
默认值为to_csv.QUOTE_MINIMAL。如果设置了浮点格式，那么浮点将转换为字符串，因此csv.QUOTE_NONNUMERIC会将它们视为非数值的。

quotechar : string (length 1), default ‘”’
字符串（长度1），默认“”
用于引用字段的字符

doublequote : boolean, default True
布尔，默认为Ture
控制一个字段内的quotechar

escapechar : string (length 1), default None
字符串（长度为1），默认为None
在适当的时候用来转义sep和quotechar的字符

chunksize : int or None
int或None
一次写入行

tupleize_cols : boolean, default False
布尔值 ，默认为False
从版本0.21.0中删除：此参数将被删除，并且总是将多索引的每行写入CSV文件中的单独行
（如果值为false）将多索引列作为元组列表（如果TRUE）或以新的、扩展的格式写入，其中每个多索引列是CSV中的一行。

date_format : string, default None
字符串，默认为None
字符串对象转换为日期时间对象

decimal: string, default ‘.’
字符串，默认’。’
字符识别为小数点分隔符。例如。欧洲数据使用’，’
"""
