#include "lists.h"

/**
 *check_cycle - a function that checks if a singly linked list has a cycle
 *@list: linked list
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *temp = list;

	if (!list)
	{
		return (0);
	}

	while (ptr && temp && temp->next)
	{
		ptr = ptr->next;
		temp = temp->next->next;
		if (ptr == temp)
			return (1);
	}

	return (0);
}
