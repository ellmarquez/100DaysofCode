#! /usr/local/bin/python3

def board(): 
    print ("""
    +---+
    |
    |
    |
    |
    =======
    """)

def head():
    print ("""
    +---+
    |   O
    |
    |
    |
    =======
    """)

def body():
    print ("""
    +---+
    |   O
    |   |
    |
    |
    =======
    """)

def rarm():
 print ("""
    +---+
    |   O
    |  \|
    |
    |
    =======
    """)

def larm():
    print ("""
    +---+
    |   O
    |  \|/
    |
    |
    =======
    """)

def lleg():
    print ("""
    +---+
    |   O
    |  \|/
    |  /
    |
    =======
    """)

def rleg():
    print ("""
    +---+
    |   O
    |  \|/
    |  / \
    |
    =======
    You Lose!
    """)