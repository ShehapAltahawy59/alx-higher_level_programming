#include "lists.h"

/**
 * get_dnodeint_at_index - get node at index
 * @head:pointer
 * @index:the index
 *
 * Return: pointer to node.
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *new;
	unsigned int i;

	new = head;
	for (i = 0; i <= index; i++)
	{
		if (new == NULL)
		{
			return (NULL);
		}
		new = new->next;
	}
	return (new);
}
