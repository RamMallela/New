#include <mutex>
#include <vector>

class MCSLockNode {
public:
    MCSLockNode() : flag_(false), next_(nullptr) {}

    std::mutex lock_;
    bool flag_;
    MCSLockNode* next_;
};

class HierarchicalMCSLock {
public:
    HierarchicalMCSLock(int num_levels) : levels_(num_levels, nullptr) {}

    void acquire() {
        for (int i = 0; i < levels_.size(); i++) {
            MCSLockNode* node = get_or_create_node(i);
            MCSLockNode* pred = get_or_create_node(i-1, node);
            node->flag_ = true;
            pred->next_ = node;
            while (node->flag_) {}
        }
    }

    void release() {
        for (int i = levels_.size() - 1; i >= 0; i--) {
            MCSLockNode* node = levels_[i];
            MCSLockNode* pred = get_or_create_node(i-1, node);
            if (node->next_ == nullptr) {
                pred->flag_ = false;
            } else {
                node->next_->flag_ = false;
            }
        }
    }

private:
    std::vector<MCSLockNode*> levels_;

    MCSLockNode* get_or_create_node(int level, MCSLockNode* default_node = nullptr) {
        if (level < 0) {
            return nullptr;
        }
        if (levels_[level] == nullptr) {
            levels_[level] = default_node != nullptr ? default_node : new MCSLockNode();
        }
        return levels_[level];
    }
};
