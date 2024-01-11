#include "lists.h"

/**
 * insert_dnodeint_at_index - check the code
 * @h:header
 * @idx:index
 * @n:value
 *
 * Return: pointer
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_node, *pointer, *prev;
	unsigned int i;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = n;
	pointer = *h;
	if (idx == 0)
	{
	new_node->prev = NULL;
	new_node->next = *h;
	if (*h != NULL)
	{
		(*h)->prev = new_node;
	}
	*h = new_node;
	return (new_node);
	}
	for (i = 0; i < idx; i++)
	{
		if (pointer == NULL)
		{
			free(new_node);
			return (NULL);
		}
		pointer = pointer->next;
	}
	new_node->prev = pointer->prev;
	new_node->next = pointer;
	pointer->prev = new_node;
	prev = new_node->prev;
	prev->next = new_node;
	return (new_node);
}
