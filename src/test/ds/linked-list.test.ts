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

  it('should merge two linkedLists', () => {
    const list1 = new LinkedList<number>();
    const list2 = new LinkedList<number>();
    list1.push(1);
    list1.push(2);
    list1.push(4);
    list2.push(1);
    list2.push(3);
    list2.push(4);
    const newList = list1.merge(list1, list2);
    let curr = newList?.first;
    const linkedListData = [];
    while (curr) {
      linkedListData.push(curr.data);
      curr = curr.next;
    }
    expect(linkedListData).toEqual([1, 1, 2, 3, 4, 4]);
  });

  it('should return empty list if two linkedLists are empty', () => {
    const list1 = new LinkedList<number>();
    const list2 = new LinkedList<number>();
    const newList = list1.merge(list1, list2);

    expect(newList?.first).toBeNull();
  });
});
