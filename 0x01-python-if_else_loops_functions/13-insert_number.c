#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to head of list
 * @number: value number member of new node to add to linked list
 *
 * Return: adress of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newnode = NULL;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	while (current->next->n < newnode->n && current->next != NULL)
		current = current->next;
	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
