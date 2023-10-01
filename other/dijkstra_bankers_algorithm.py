# A Python implementation of the Banker's Algorithm in Operating Systems using
# Processes and Resources
# {
# "Author: "Biney Kingsley (bluedistro@github.io), bineykingsley36@gmail.com",
# "Date": 28-10-2018
# }
"""
The Banker's algorithm is a resource allocation and deadlock avoidance algorithm
developed by Edsger Dijkstra that tests for safety by simulating the allocation of
predetermined maximum possible amounts of all resources, and then makes a "s-state"
check to test for possible deadlock conditions for all other pending activities,
before deciding whether allocation should be allowed to continue.
[Source] Wikipedia
[Credit] Rosetta Code C implementation helped very much.
 (https://rosettacode.org/wiki/Banker%27s_algorithm)
"""

from __future__ import annotations

import time

import numpy as np
from typing import List

test_claim_vector = [8, 5, 9, 7]
test_allocated_res_table = [
    [2, 0, 1, 1],
    [0, 1, 2, 1],
    [4, 0, 0, 3],
    [0, 2, 1, 0],
    [1, 0, 3, 0],
]
test_maximum_claim_table = [
    [3, 2, 1, 4],
    [0, 2, 5, 2],
    [5, 1, 0, 5],
    [1, 5, 3, 0],
    [3, 0, 3, 3],
]
































class BankersAlgorithm:
    def __init__(
        self,
        claim_vector: list[int],
        allocated_resources_table: list[list[int]],
        maximum_claim_table: list[list[int]],
    ) -> None:
        """
        :param claim_vector: A nxn/nxm list depicting the amount of each resources
         (eg. memory, interface, semaphores, etc.) available.
        :param allocated_resources_table: A nxn/nxm list depicting the amount of each
         resource each process is currently holding
        :param maximum_claim_table: A nxn/nxm list depicting how much of each resource
         the system currently has available
        """
        self.__claim_vector = claim_vector
        self.__allocated_resources_table = allocated_resources_table
        self.__maximum_claim_table = maximum_claim_table

    def __processes_resource_summation(self) -> list[int]:
        """
        Compute the sum of allocated resources for each resource in the claim vector.

        This method traverses the table of allocated resources and sums up the quantities
        of each individual resource across all processes. The result is a list where each
        entry corresponds to total quantity of a specific resource that has been allocated
        to all processes.

        Returns:
            list[int]: A list of integers where each integer is the total allocation of a
                       specific resource across all processes.
        """
        return [
            sum(p_item[i] for p_item in self.__allocated_resources_table)
            for i in range(len(self.__allocated_resources_table[0]))
        ]

    def __available_resources(self) -> list[int]:
        """
        Check for available resources in line with each resource in the claim vector
        """
        return np.array(self.__claim_vector) - np.array(
            self.__processes_resource_summation()
        )

    def __need(self) -> list[list[int]]:
        """
        Implement safety checker that calculates the needs by ensuring that
        max_claim[i][j] - alloc_table[i][j] <= avail[j]
        """
        return [
            list(np.array(self.__maximum_claim_table[i]) - np.array(allocated_resource))
            for i, allocated_resource in enumerate(self.__allocated_resources_table)
        ]

    def __need_index_manager(self) -> dict[int, list[int]]:
        """
        This function builds an index control dictionary to track original ids/indices
        of processes when altered during execution of method "main"
            Return: {0: [a: int, b: int], 1: [c: int, d: int]}
        >>> (BankersAlgorithm(test_claim_vector, test_allocated_res_table,
        ...     test_maximum_claim_table)._BankersAlgorithm__need_index_manager()
        ...     )  # doctest: +NORMALIZE_WHITESPACE
        {0: [1, 2, 0, 3], 1: [0, 1, 3, 1], 2: [1, 1, 0, 2], 3: [1, 3, 2, 0],
         4: [2, 0, 0, 3]}
        """
        return {self.__need().index(i): i for i in self.__need()}

    def main(self, **kwargs) -> None:
        """
        Executes the Banker's Algorithm simulation.

        Accepts variable keyword arguments for configuration (though implementation is not shown here).
        It computes the "need" of each process, checks available resources, and makes sure that the system is in a safe state after each
        iteration. If it detects that the system is in an unsafe state, it aborts the simulation.

        Args:
            kwargs: Variable keyword arguments for configuration purposes.

        Returns:
            None

        Raises:
            SystemError: If the system is in an unsafe state.

        Output:
            Detailed process execution information, including which process is executing and
            how resources are being allocated and updated.

        Usage:
        >>> BankersAlgorithm(test_claim_vector, test_allocated_res_table,
        ...    test_maximum_claim_table).main(describe=True)
        """
        need_list = self.__need()
        alloc_resources_table = self.__allocated_resources_table
        available_resources = self.__available_resources()
        need_index_manager = self.__need_index_manager()
        for kw, val in kwargs.items():
            if kw and val is True:
                self.__pretty_data()
        print("_" * 50 + "\n")
        while need_list:
            safe = False
            for each_need in need_list:
                execution = True
                for index, need in enumerate(each_need):
                    if need > available_resources[index]:
                        execution = False
                        break
                if execution:
                    safe = True
                    # get the original index of the process from ind_ctrl db
                    for original_need_index, need_clone in need_index_manager.items():
                        if each_need == need_clone:
                            process_number = original_need_index
                    print(f"Process {process_number + 1} is executing.")
                    # remove the process run from stack
                    need_list.remove(each_need)
                    # update available/freed resources stack
                    available_resources = np.array(available_resources) + np.array(
                        alloc_resources_table[process_number]
                    )
                    print(
                        "Updated available resource stack for processes: "
                        + " ".join([str(x) for x in available_resources])
                    )
                    break
            if safe:
                print("The process is in a safe state.\n")
            else:
                print("System in unsafe state. Aborting...\n")
                break

    def __pretty_data(self, data: List[List[int]]) -> str:
        """Returns a formatted string for presenting the 2D list `data`.

        Args:
            data: A list of lists, each representing a row of data.

        Returns:
            A string where each `data` row is separated with a newline character,
            and each entry inside a row is separated by a space.
        """
        return "\n".join(" ".join(map(str, row)) for row in data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
