/**
 * Linked List
 * 
 * @example
 * const linkedList = require('linked-list');
 * 
 * @author Gaurav Soni
 * 
 * @module ds/linked-list
 * 
 */
// (function (exports) {

/**
 * A node inside a linked list.
 * 
 * @public
 * @constructor
 * 
 * @param {unknown} data - The value stored in the linked list
 */
export class ListNode<T> {
    /**
     * Data of the list node.
     * @member {Object}
     */
    public data!: T;
    /**
     * Next node
     * @member {ListNode}
     */
    next: ListNode<T> | null = null;
    /**
     * Previous node
     * @member {ListNode}
     */
    prev: ListNode<T> | null = null;

    constructor(data: T) {
        this.data = data;
    }

}

/**
 * Linked list
 * 
 * 
 * @public
 * @constructor
 */
export class LinkedList<T> {
    first: ListNode<T> | null = null;
    last: ListNode<T> | null = null;

    push(data: T) {
        const node = new ListNode(data);
        if (!this.first) {
            this.first = this.last = node;
        } else {
            const temp = this.last as ListNode<T>;
            this.last = node;
            temp.next = node;
        }
    }

    /**
     * Given the head of a singly linked list, reverse the list, and return the reversed list.
     * <br />
     * For example, 
     * <br />
     * <b>Input:</b> 1 -> 2 -> 3 -> 4 -> 5
     * <br />
     * <b>Output:</b> 5 -> 4 -> 3 -> 2 -> 1
     * <br />
     * 
     * @method
     * @see {@link https://leetcode.com/problems/reverse-linked-list/|Reverse Linked List}
     * 
     * @public
     * 
     * @param {ListNode} head Head of linked list
     * @returns {ListNode} Reversed linked list
     */

    reverse(): ListNode<T> | null {
        if (!this.first || !this.first.next) {
            return null;
        }
        let prev = null;
        let curr = this.first;
        while (curr !== null) {
            const temp = curr.next as ListNode<T>;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        const temp = this.first;
        this.first = this.last;
        this.last = temp;
        return this.first;
    }

    /**
     * Given the head of a singly linked list, reverse the list, and return the reversed list.
     * <br />
     * For example, 
     * <br />
     * <b>Input:</b> 1 -> 2 -> 3 -> 4 -> 5
     * <br />
     * <b>Output:</b> 5 -> 4 -> 3 -> 2 -> 1
     * <br />
     * 
     * @method
     * @see {@link https://leetcode.com/problems/reverse-linked-list/|Reverse Linked List}
     * 
     * @public
     * 
     * @param {ListNode} head Head of linked list
     * @returns {ListNode} Reversed linked list
     */

    recursiveReverse(): ListNode<T> | null {
        function inverse(head: ListNode<T> | null): ListNode<T> | null {
            if (!head || !head.next) {
                return null;
            }
            const newFirst = inverse(head.next);
            head.next.next = head;
            head.next = null;
            return newFirst;
        }
        if (!this.first) {
            return null;
        }
        inverse(this.first);
        const temp = this.first;
        this.first = this.last;
        this.last = temp;
        return this.first;
    }
}
