#include "lists.h"
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check palinfrom
 * @head: the head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}
	else
	{
		listint_t *new = *head, *last = *head;
		int counter = 0, i;

		while (last->next != NULL)
		{
			counter = counter + 1;
			last = last->next;
		}
		last = *head;

		for (i = 0; i < counter / 2; i++)
		{
			last = last->next;
		}
		while (last != NULL)
		{
			if (last->n != new->n)
			{
				return (0);
			}
			last = last->next;
			new = new->next;

		}
		return (1);
	}
}
