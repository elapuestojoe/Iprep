#include <iostream>
#include <cstdio>

using namespace std;

struct node {
    int data;
    node *next;
};

class LinkedList{
    private:
    node *head, *tail;
    public:
    LinkedList() {
        head=NULL;
        tail=NULL;
    }

    void createNode(int value) {
        node *temp = new node;
        temp->data = value;
        temp->next = NULL;
        if(head == NULL){
            head = temp;
            tail = temp;
            temp = NULL;
        } else {
            tail->next = temp;
            tail = temp;
        }
    }

    void display() {
        node *temp = new node;
        temp = head;
        while(temp != NULL) {
            cout << temp->data<<"\t";
            temp = temp->next;
        }
    }
};

void createNode(int value);

int main() {
    LinkedList linkedList;
    linkedList.display();
    linkedList.createNode(3);
    linkedList.createNode(5);
    linkedList.display();
    
}