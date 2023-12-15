#include <mutex>
#include <queue>
#include <condition_variable>
#include <chrono>

class QueueLockWithTimeout {
public:
    void acquire(std::chrono::milliseconds timeout) {
        std::unique_lock<std::mutex> lock(mutex_);
        queue_.push(std::this_thread::get_id());
        if (!cv_.wait_for(lock, timeout, [this]() { return queue_.front() == std::this_thread::get_id(); })) {
            queue_.pop();
            throw std::runtime_error("Timeout waiting for lock");
        }
    }

    void release() {
        std::lock_guard<std::mutex> lock(mutex_);
        queue_.pop();
        cv_.notify_one();
    }

private:
    std::mutex mutex_;
    std::queue<std::thread::id> queue_;
    std::condition_variable cv_;
};
