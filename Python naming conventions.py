module_name, package_name, ClassName, method_name, ExceptionName, 
function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, 
function_parameter_name, local_var_name


Tab = 4 spaces

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)


# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)


#  limiting lines to 79 characters
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())


# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# Import modules
Yes: import os
     import sys

# Avoid extraneous whitespace in the following situations:
Yes: spam(ham[1], {eggs: 2})
Yes: foo = (0,)
Yes: if x == 4: print x, y; x, y = y, x
Yes: spam(1)
Yes: dct['key'] = lst[index]
