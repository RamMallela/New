#include <mutex>
#include <condition_variable>
#include <thread>
#include <vector>

class CohortLock {
public:
    CohortLock(int num_threads) : num_threads_(num_threads), num_arrived_(0), cohort_ready_(false), mutex_(), cv_() {}

    void acquire() {
        std::unique_lock<std::mutex> lock(mutex_);
        int cohort_num = cohort_num_;
        num_arrived_++;
        if (num_arrived_ < num_threads_) {
            while (cohort_num_ == cohort_num && !cohort_ready_) {
                cv_.wait(lock);
            }
        } else {
            cohort_ready_ = true;
            cohort_num_++;
            num_arrived_ = 0;
            cv_.notify_all();
        }
    }

    void release() {
        std::unique_lock<std::mutex> lock(mutex_);
        cohort_ready_ = false;
        cv_.notify_all();
    }

private:
    int num_threads_;
    int num_arrived_;
    int cohort_num_;
    bool cohort_ready_;
    std::mutex mutex_;
    std::condition_variable cv_;
};
