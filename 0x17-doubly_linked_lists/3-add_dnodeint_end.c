#include "lists.h"

/**
 * add_dnodeint_end - add node at end
 * @head: the header
 * @n:the vakue
 *
 * Return: the value.
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node, *prev;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	prev = *head;
	while (prev->next != NULL)
	{
		prev = prev->next;
	}
	new_node->prev = prev;
	new_node->next = NULL;
	new_node->n = n;
	return (new_node);
}
