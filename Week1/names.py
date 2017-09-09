"""Coding Dojo - Python Fundamentals - Assignment: Names

Created: 09/03/2017
Author: Frank J Genova

Part I
Given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Create a program that outputs:
Michael Jordan
John Rosales
Mark Guillen
KB Tonel

Part II
Now, given the following dictionary:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
Create a program that prints the following format
(including number of characters in each combined name):
Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13

"""



def main():
    """Print students"""

    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    print("="*80)
    for student in students:
        first_name = student['first_name']
        last_name = student['last_name']
        print("{} {}".format(first_name, last_name))
    print("="*80)

    users = {
        'Students': [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ],
        'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
        ]
    }

    print("="*80)
    for kind in users:
        print(kind)
        count = 0
        character_count = 0
        for each in users[kind]:
            count += 1
            first_name = each['first_name']
            character_count = len(first_name)
            last_name = each['last_name']
            character_count += len(last_name)
            print("{} - {} {} - {}".format(count, first_name, last_name, character_count))
    print("="*80)

if __name__ == '__main__':
    main()
    