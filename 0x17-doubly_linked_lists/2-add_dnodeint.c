#include "lists.h"

/**
 * add_dnodeint - add node
 * @n:the value
 * @head:pointer to head
 * Return: pointer to node.
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}


	new_node->next = *head;
	new_node->n = n;
	new_node->prev = NULL;

	(*head)->prev = new_node;
	return (new_node);
}
