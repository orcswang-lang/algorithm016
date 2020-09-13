type MyCircularDeque struct {
    cache []int
    capacity int
    length int
    front int
    rear int
}


/** Initialize your data structure here. Set the size of the deque to be k. */
func Constructor(k int) MyCircularDeque {
    return MyCircularDeque{
        cache: make([]int, k),
        capacity: k,
        front: 1,
    }
}


/** Adds an item at the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertFront(value int) bool {
    if this.length == this.capacity {
        return false
    }
    this.length++
    this.front--
    if this.front == -1 {
        this.front = this.capacity - 1
    }
    this.cache[this.front] = value
    return true
}


/** Adds an item at the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertLast(value int) bool {
    if this.length == this.capacity {
        return false
    }
    this.length++
    this.rear++
    if this.rear == this.capacity {
        this.rear = 0
    }
    this.cache[this.rear] = value
    return true
}


/** Deletes an item from the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteFront() bool {
    if this.length == 0 {
        return false
    }
    this.length--
    this.front++
    if this.front == this.capacity {
        this.front = 0
    }
    return true
}


/** Deletes an item from the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteLast() bool {
    if this.length == 0 {
        return false
    }
    this.length--
    this.rear--
    if this.rear == -1 {
        this.rear = this.capacity - 1
    }
    return true
}


/** Get the front item from the deque. */
func (this *MyCircularDeque) GetFront() int {
    if this.length == 0 {
        return -1
    }
    return this.cache[this.front]
}


/** Get the last item from the deque. */
func (this *MyCircularDeque) GetRear() int {
    if this.length == 0 {
        return -1
    }
    return this.cache[this.rear]
}


/** Checks whether the circular deque is empty or not. */
func (this *MyCircularDeque) IsEmpty() bool {
    return this.length == 0
}


/** Checks whether the circular deque is full or not. */
func (this *MyCircularDeque) IsFull() bool {
    return this.length == this.capacity
}


/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */