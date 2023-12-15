#include <mutex>
#include <vector>
#include <chrono>
#include <thread>

class HierarchicalBackoffLock {
public:
    HierarchicalBackoffLock(int num_levels) : locks_(num_levels) {}

    void acquire() {
        for (int i = locks_.size() - 1; i >= 0; i--) {
            if (locks_[i].try_lock()) {
                return;
            }
        }
        backoff();
        acquire();
    }

    void release() {
        for (int i = 0; i < locks_.size(); i++) {
            if (locks_[i].owns_lock()) {
                locks_[i].unlock();
                return;
            }
        }
    }

private:
    std::vector<std::mutex> locks_;

    void backoff() {
        // TODO: Implement a backoff strategy
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
};
