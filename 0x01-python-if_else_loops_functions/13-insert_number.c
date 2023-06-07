#include "lists.h"

/**
 * insert_node - Inserts a number into a linked list.
 * @head: A pointer the head
 * @number: The number to insert.
 * Return: If it fails - NULL, otherwise - pointer to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (ptr == NULL || ptr->n >= number)
	{
		new->next = ptr;
		*head = new;
		return (new);
	}

	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;

	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
