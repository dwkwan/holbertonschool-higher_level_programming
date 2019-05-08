#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check if listint_t linked list is a palindrome
 * @head: a pointer to a pointer to a struct
 *
 * Return: 1 if palindrome, else 0
 */
listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *tmp = NULL;

	if (!*head)
		return (1);
	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow = reverse_list(&slow);
	tmp = slow;
	fast = *head;
	while (slow && fast)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	reverse_list(&tmp);
	return (1);
}
/**
 * reverse_list - reverses a listint_t linked list
 * @head: a pointer to a pointer to a struct
 *
 * Return: a pointer to first node of reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *ahead = NULL;

	while (*head)
	{
		ahead = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = ahead;
	}
	*head = prev;
	return (*head);
}
