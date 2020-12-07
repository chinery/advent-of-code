#include "Solver.hpp"
#include <string>
#include <vector>
#include <memory>
#include <map>

class BagGraphNode {
private:
    std::string m_Name;

    std::vector<std::shared_ptr<BagGraphNode>> m_Parents;

    std::vector<int> m_Counts;
    std::vector<std::shared_ptr<BagGraphNode>> m_Children;
public:
    BagGraphNode(const std::string& name);

    const std::string& getName() const;
    const std::vector<std::shared_ptr<BagGraphNode>>& getParents() const;
    const std::vector<std::shared_ptr<BagGraphNode>>& getChildren() const;
    const std::vector<int>& getCounts() const;

    void addChild(int count, std::shared_ptr<BagGraphNode> child);
    void addParent(std::shared_ptr<BagGraphNode> parent);

};

class BagGraph {
private:
    std::map<std::string, std::shared_ptr<BagGraphNode>> m_Lookup;
public:
    BagGraph();

    void addNode(const std::string& name);
    void addChild(const std::string& parent, int count, const std::string& child);
    
    int countUniqueBagsUp(const std::string& bag) const;
    int countNumberBagsDown(const std::string& bag) const;
    int countNumberBagsDown(const std::shared_ptr<BagGraphNode>& ptr) const;
};

class Day7 : public Solver {
public:
    Day7();
    std::string runPart1(const std::vector<std::string>& input) override;
    std::string runPart2(const std::vector<std::string>& input) override;
private:
    BagGraph buildGraph(const std::vector<std::string>& input);
};