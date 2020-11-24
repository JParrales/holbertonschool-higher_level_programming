#include "lists.h"

int is_palindrome(listint_t **head)
{
	int size;
	int op[2048];
	int i;

	size = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (*head != NULL)
	{
		size++;
		op[size -1] = (*head)->n;
		head = &(*head)->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (op[i] != op[size - 1 - i])
			return (0);
	}

	return (1);

}
