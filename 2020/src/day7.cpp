#include "day7.hpp"
#include "util.hpp"
#include <set>
#include <list>
#include <algorithm>
#include <iostream>

/*
 * BagGraph Class
 */ 
BagGraph::BagGraph() : m_Lookup() {};

int BagGraph::countUniqueBagsUp(const std::string& bag) const {
    int count = -1;
    std::shared_ptr<BagGraphNode> startPtr = m_Lookup.at(bag);

    std::list<std::shared_ptr<BagGraphNode>> frontier;
    frontier.push_back(startPtr);

    std::set<std::string> counted;
    std::shared_ptr<BagGraphNode> ptr;

    while(frontier.size() > 0) {
        ptr = frontier.front();
        frontier.pop_front();

        count++;
        counted.insert(ptr->getName());

        for(auto node : ptr->getParents()) {
            if(counted.find(node->getName()) == counted.end()
                && std::find(frontier.begin(), frontier.end(), node) == frontier.end()){
                frontier.push_back(node);
            }
        }
    }
    return count;
}

int BagGraph::countNumberBagsDown(const std::shared_ptr<BagGraphNode>& ptr) const {
    auto children = ptr->getChildren();
    if(children.size() == 0) {
        return 0;
    } else{
        auto counts = ptr->getCounts();
        int total = 0;
        for(int i = 0; i < children.size(); i++){
            auto child = children[i];
            total += counts[i];

            total += counts[i] * countNumberBagsDown(child);
        }
        return total;
    }
}

int BagGraph::countNumberBagsDown(const std::string& bag) const {
    std::shared_ptr<BagGraphNode> ptr = m_Lookup.at(bag);

    return countNumberBagsDown(ptr);
}

void BagGraph::addNode(const std::string& name) {
    if(m_Lookup.find(name) == m_Lookup.end()) {
        m_Lookup[name] = std::make_shared<BagGraphNode>(name);
    }
}

void BagGraph::addChild(const std::string& parent, int count, const std::string& child) {
    std::shared_ptr<BagGraphNode> childPtr;
    if(m_Lookup.find(child) == m_Lookup.end()) {
        childPtr = std::make_shared<BagGraphNode>(child);
        m_Lookup[child] = childPtr;
    } else {
        childPtr = m_Lookup[child];
    }

    auto parentPtr = m_Lookup[parent];
    parentPtr->addChild(count, childPtr);
    childPtr->addParent(parentPtr);
}

/*
 * BagGraphNode Class
 */ 
BagGraphNode::BagGraphNode(const std::string& name) : 
    m_Name(name) {}

const std::string& BagGraphNode::getName() const {
    return m_Name;
}

const std::vector<std::shared_ptr<BagGraphNode>>& BagGraphNode::getParents() const {
    return m_Parents;
}

const std::vector<std::shared_ptr<BagGraphNode>>& BagGraphNode::getChildren() const {
    return m_Children;
}

const std::vector<int>& BagGraphNode::getCounts() const {
    return m_Counts;
}

void BagGraphNode::addParent(std::shared_ptr<BagGraphNode> parent) {
    m_Parents.push_back(parent);
}

void BagGraphNode::addChild(int count, std::shared_ptr<BagGraphNode> child) {
    m_Counts.push_back(count);
    m_Children.push_back(child);
}

/*
 * Day7 Class
 */ 
Day7::Day7() : Solver("day7") {}

BagGraph Day7::buildGraph(const std::vector<std::string>& input) {
    BagGraph graph = BagGraph();
    for(std::string line : input){
        std::vector<std::string> splitString = util::split(line, ' ');

        std::string name = splitString[0] + " " + splitString[1];

        graph.addNode(name);

        if(splitString[4] == "no"){
            continue;
        } else {
            int count = (splitString.size() - 4)/4;
            for(int i = 0; i < count; i++){
                int start = 4 + (i*4);
                int number = std::stoi(splitString[start]);
                std::string childName = splitString[start + 1] + " " + splitString[start + 2];

                graph.addChild(name, number, childName);
            }
        }
    }
    return graph;
}

std::string Day7::runPart1(const std::vector<std::string>& input) {
    BagGraph graph = buildGraph(input);
    return std::to_string(graph.countUniqueBagsUp("shiny gold"));
}

std::string Day7::runPart2(const std::vector<std::string>& input) {
    BagGraph graph = buildGraph(input);
    return std::to_string(graph.countNumberBagsDown("shiny gold"));
}