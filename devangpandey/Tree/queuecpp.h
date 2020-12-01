#include <bits/stdc++.h>

using namespace std;

class Node
{
public:
    int data;
    Node *lchild;
    Node *rchild;
};

class Stack
{
    int size;
    int top;
    Node** st;

public:
    Stack()
    {
        size = 10;
        top = -1;
        st = new Node*[size];
    }
    Stack(int x)
    {
        this->size = x;
        top = -1;
        st = new Node*[this->size];
    }
    void push(Node* x);
    Node* pop();
    int isEmpty();
    void display();
};

void Stack::push(Node* x)
{
    if (top == size - 1)
        cout << "Full";
    else
    {
        top++;
        st[top] = x;
    }
}

Node* Stack::pop()
{
    Node* temp = NULL;
    if (top == -1)
        cout << "Empty";
    else
    {
        temp = st[top];
        top--;
    }
    return temp;
}

int Stack::isEmpty()
{
    return top == -1;
}

class Queue
{
private:
    int front;
    int rear;
    int size;
    Node **Q;

public:
    Queue()
    {
        front = rear = -1;
        size = 10;
        Q = new Node *[size];
    }
    Queue(int size)
    {
        front = rear = -1;
        this->size = size;
        Q = new Node *[this->size];
    }
    void enqueue(Node *x);
    Node *dequeue();
    int isEmpty()
    {
        return front == rear;
    }
    void display();
};

void Queue::enqueue(Node *x)
{
    if (rear == size - 1)
        cout << "Queue is full";
    else
    {
        rear++;
        Q[rear] = x;
    }
}

Node *Queue::dequeue()
{
    Node *x = NULL;
    if (rear == front)
    {
        cout << "Empty";
    }
    else
    {
        x = Q[front + 1];
        front++;
    }
    return x;
}

void Queue::display()
{
    for (int i = front + 1; i <= rear; i++)
    {
        cout << Q[i] << endl;
    }
}
