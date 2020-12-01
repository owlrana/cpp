#include "queuecpp.h"
#include<bits/stdc++.h>
using namespace std;

Node *root = NULL;

void createTree()
{
    int x;
    Queue q(100);
    Node *t, *p;
    root = new Node();
    cout << "Enter root ";
    cin >> root->data;
    root->lchild = root->rchild = NULL;
    q.enqueue(root);
    while (!q.isEmpty())
    {
        p = q.dequeue();
        cout << "Enter left child of " << p->data << " ";
        cin >> x;
        if (x != -1)
        {
            t = new Node();
            t->data = x;
            t->lchild = t->rchild = NULL;
            p->lchild = t;
            q.enqueue(t);
        }

        cout << "Enter right child of " << p->data << " ";
        cin >> x;
        if (x != -1)
        {
            t = new Node();
            t->data = x;
            t->lchild = t->rchild = NULL;
            p->rchild = t;
            q.enqueue(t);
        }
    }
}
void preorder(Node *p)
{
    Stack st(100);
    while (p || !st.isEmpty())
    {
        if (p != NULL)
        {
            cout << p->data << endl;
            st.push(p);
            p = p->lchild;
        }
        else
        {
            p = st.pop();
            p = p->rchild;
        }
    }
}

void levelorderTraversal(Node *root)
{
    Queue q(100);
    Node *p;
    p = root;
    cout << p->data << " ";
    q.enqueue(p);
    while (!q.isEmpty())
    {
        p = q.dequeue();
        if (p->lchild)
        {
            cout << p->lchild->data << " ";
            q.enqueue(p->lchild);
        }
        if (p->rchild)
        {
            cout << p->rchild->data << " ";
            q.enqueue(p->rchild);
        }
    }
}

void inOrder(Node *root)
{
    Stack st(100);
    Node *t;
    t = root;
    while (t || !st.isEmpty())
    {
        if (t != NULL)
        {
            st.push(t);
            t = t->lchild;
        }
        else
        {
            t = st.pop();
            cout << t->data << " ";
            t = t->rchild;
        }
    }
}

void IpostOrderTraversal(Node *root)
{
    if (root==NULL)
    return ;
    Stack st1(100);
    Stack st2(100);
    Node *p;
    st1.push(root);
    while(!st1.isEmpty())
    {
       p=st1.pop();
        st2.push(p);
        if(p->lchild!=NULL)
        {
            st1.push(p->lchild);
        }
        if(p->rchild!=NULL)
        {
            st1.push(p->rchild);
        }
    }
    while(!st2.isEmpty())
    {
        Node *temp;
        temp=st2.pop();
        cout<<temp->data<<' ';
    }
}

int countNodes(Node *root)
{
    int x = 0, y = 0;
    Node *p = root;

    if (p)
    {
        x = countNodes(p->lchild);
        y = countNodes(p->rchild);
        if (p->lchild && p->rchild)
            return x + y + 1;
        else
            return x + y;
    }
    return 0;
}

int main()
{
    createTree();
    IpostOrderTraversal(root);
}

