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
	if (!*head)
	{
		*head = newnode;
		return (newnode);
	}
	if (newnode->n < current->next->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (current->next != NULL && current->next->n < newnode->n)
		current = current->next;
	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
