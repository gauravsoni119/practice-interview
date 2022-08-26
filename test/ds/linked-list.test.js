"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const linked_list_1 = require("../../ds/linked-list");
describe('Node', () => {
    it('should  create a Node', () => {
        const node = new linked_list_1.ListNode('some data');
        expect(node.data).toEqual('some data');
    });
});
describe('ListNode', () => {
    it('should create a Node', () => {
        const node = new linked_list_1.ListNode('some data');
        expect(node.data).toEqual('some data');
    });
});
describe('LinkedList', () => {
    it('should insert items into linkedList', () => {
        var _a, _b;
        const list = new linked_list_1.LinkedList();
        list.push(1);
        list.push(2);
        list.push(3);
        expect((_a = list.last) === null || _a === void 0 ? void 0 : _a.data).toEqual(3);
        expect((_b = list.first) === null || _b === void 0 ? void 0 : _b.data).toEqual(1);
    });
    it('should reverse items in linkedList', () => {
        var _a, _b;
        const list = new linked_list_1.LinkedList();
        list.push(1);
        list.push(2);
        list.push(3);
        list.reverse();
        expect((_a = list.last) === null || _a === void 0 ? void 0 : _a.data).toEqual(1);
        expect((_b = list.first) === null || _b === void 0 ? void 0 : _b.data).toEqual(3);
    });
    it('should reverse items recursively in linkedList', () => {
        var _a, _b;
        const list = new linked_list_1.LinkedList();
        list.push(1);
        list.push(2);
        list.push(3);
        list.recursiveReverse();
        expect((_a = list.last) === null || _a === void 0 ? void 0 : _a.data).toEqual(1);
        expect((_b = list.first) === null || _b === void 0 ? void 0 : _b.data).toEqual(3);
    });
    it('should merge two linkedLists', () => {
        const list1 = new linked_list_1.LinkedList();
        const list2 = new linked_list_1.LinkedList();
        list1.push(1);
        list1.push(2);
        list1.push(4);
        list2.push(1);
        list2.push(3);
        list2.push(4);
        const newList = list1.merge(list1, list2);
        let curr = newList === null || newList === void 0 ? void 0 : newList.first;
        const linkedListData = [];
        while (curr) {
            linkedListData.push(curr.data);
            curr = curr.next;
        }
        expect(linkedListData).toEqual([1, 1, 2, 3, 4, 4]);
    });
    it('should return empty list if two linkedLists are empty', () => {
        const list1 = new linked_list_1.LinkedList();
        const list2 = new linked_list_1.LinkedList();
        const newList = list1.merge(list1, list2);
        expect(newList === null || newList === void 0 ? void 0 : newList.first).toBeNull();
    });
});
