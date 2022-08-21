import { ListNode, LinkedList } from '../../ds/linked-list';
describe('Node', () => {
    it('should  create a Node', () => {
        const node = new ListNode('some data');
        expect(node.data).toEqual('some data');
    });
});

describe('ListNode', () => {
    it('should create a Node', () => {
        const node = new ListNode('some data');
        expect(node.data).toEqual('some data');
    });
});

describe('LinkedList', () => {
    it('should insert items into linkedList', () => {
        const list = new LinkedList<number>();
        list.push(1);
        list.push(2);
        list.push(3);
        expect(list.last?.data).toEqual(3);
        expect(list.first?.data).toEqual(1);
    });

    it('should reverse items in linkedList', () => {
        const list = new LinkedList<number>();
        list.push(1);
        list.push(2);
        list.push(3);
        list.reverse();
        expect(list.last?.data).toEqual(1);
        expect(list.first?.data).toEqual(3);
    });

    it('should reverse items recursively in linkedList', () => {
        const list = new LinkedList<number>();
        list.push(1);
        list.push(2);
        list.push(3);
        list.recursiveReverse();
        expect(list.last?.data).toEqual(1);
        expect(list.first?.data).toEqual(3);
    });
});