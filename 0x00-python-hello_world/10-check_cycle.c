#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * @list: List to be checked
 * Return: 0 if cycle does not exist
 *         1 if cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *quick = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (1)
	{
		/*traverse through nodes as long as linked list node exists*/
		if (quick->next != NULL && quick->next->next != NULL)
		{
			quick = quick->next->next;
			slow = slow->next;

			if (quick == slow) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
