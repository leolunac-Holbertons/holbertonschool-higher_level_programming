#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
*
* @head: double pointer to first node of linked list
* Return: 0 if not palindrome, 1 if it is
*/
int is_palindrome(listint_t **head)
{
	unsigned int len = 1, i;
	listint_t *end;

	if (!head || !*head || (*head)->next == NULL)
		return (1);

	end = *head;

	while (end->next)
	{
		end = end->next;
		len++;
	}
	if (len % 2)
		len++;

	end = *head;

	for (i = 0; i < len / 2; i++)
	{
		if (end->next)
			end = end->next;
	}

	if (check_pali(*head, end))
		return (1);

	return (0);
}

/**
* check_pali - recursive function to check palindrome nature of list
*
* @h: head of linked list
* @e: one past mid point of list
* Return: a pointer to a node if palindrome, NULL if not
*/
listint_t *check_pali(listint_t *h, listint_t *e)
{
	if (e->next == NULL)
	{
		if (h->n == e->n)
			return (h->next);
		return (NULL);
	}
	h = check_pali(h, e->next);
	if (h && h->n == e->n)
		return (h->next);
	return (NULL);
}
