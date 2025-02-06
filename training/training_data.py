import json

# Training data covering the specified topics and keywords.
training_data = {
  "input_text": [
    # IMEx Ecosystem
    "Question: What are the key components of the IMEx Ecosystem? Context: The IMEx Ecosystem comprises interconnected systems, including data management platforms, collaboration tools, and resource allocation systems.",
    "Question: How does the IMEx Ecosystem improve resource utilization? Context: By integrating various systems, IMEx enables real-time visibility into resource availability and facilitates optimized allocation.",
    "Question: What are the benefits of the IMEx Ecosystem for collaboration? Context: IMEx fosters seamless collaboration by providing a centralized platform for information sharing and project management.",

    # Integrated Facilities Program (IFP)
    "Question: What are the core principles of the IFP? Context: The IFP is built on principles of standardization, efficiency, and continuous improvement in facilities management.",
    "Question: How does the IFP contribute to cost savings? Context: By streamlining processes and optimizing resource allocation, the IFP helps reduce operational costs.",
    "Question: What are the key performance indicators (KPIs) for the IFP? Context: KPIs for the IFP include operational efficiency, cost savings, and regulatory compliance.",

    # Compliance
    "Question: What are the different types of compliance relevant to our operations? Context: Compliance includes adherence to environmental regulations, safety standards, and industry best practices.",
    "Question: How do we ensure compliance with evolving regulations? Context: We maintain a robust compliance program that includes regular audits, training, and updates on regulatory changes.",
    "Question: What are the consequences of non-compliance? Context: Non-compliance can lead to penalties, reputational damage, and operational disruptions.",

    # Safety (Electrical Safety)
    "Question: What are the common electrical hazards in a manufacturing environment? Context: Common hazards include arc flash, electrical shock, and equipment malfunction.",
    "Question: What safety measures are in place to prevent electrical accidents? Context: We have implemented lockout/tagout procedures, regular equipment inspections, and employee training programs.",
    "Question: What is the role of personal protective equipment (PPE) in electrical safety? Context: PPE, such as insulated gloves and arc flash suits, provides an additional layer of protection against electrical hazards.",

    # Life Cycle Asset Management
    "Question: What are the stages of Life Cycle Asset Management? Context: The stages include planning, acquisition, operation, maintenance, and disposal.",
    "Question: How does Life Cycle Asset Management impact maintenance strategies? Context: It promotes proactive maintenance strategies to extend asset lifespan and minimize downtime.",
    "Question: What tools are used for Life Cycle Asset Management? Context: CMMS (Computerized Maintenance Management Systems) are commonly used to track and manage assets.",

    # Capital Planning
    "Question: What factors are considered in Capital Planning? Context: Factors include strategic goals, financial resources, risk assessment, and project prioritization.",
    "Question: How is Capital Planning aligned with business objectives? Context: Capital Planning ensures that investments support the long-term strategic direction of the organization.",
    "Question: What is the process for approving Capital Projects? Context: The approval process typically involves review by a project committee and executive leadership.",

    # OpU Engineering
    "Question: What are the key areas of focus for OpU Engineering? Context: OpU Engineering focuses on process optimization, cost reduction, and efficiency improvements.",
    "Question: How does OpU Engineering contribute to operational excellence? Context: By applying engineering principles, OpU Engineering drives continuous improvement and operational efficiency.",
    "Question: What tools and techniques are used in OpU Engineering? Context: Lean manufacturing principles, Six Sigma methodologies, and data analytics are commonly used.",

    # Environmental Engineering & Legacy Sites
    "Question: What are the challenges associated with legacy site remediation? Context: Challenges include contamination assessment, remediation technology selection, and regulatory compliance.",
    "Question: How does Environmental Engineering contribute to sustainability? Context: By remediating contaminated sites, Environmental Engineering helps protect the environment and human health.",
    "Question: What regulations govern legacy site management? Context: Various environmental regulations, specific to the location, govern legacy site management and remediation. ",

    # Business Operation & Innovation
    "Question: How can businesses foster a culture of innovation? Context: By encouraging experimentation, embracing new ideas, and providing resources for innovation.",
    "Question: What are the different types of business innovation? Context: Innovation can include product innovation, process innovation, and business model innovation.",
    "Question: How can businesses measure the success of innovation initiatives? Context: Metrics such as revenue growth, market share, and customer satisfaction can be used.",

    # Launch Excellence
    "Question: What are the critical success factors for Launch Excellence? Context: Critical factors include thorough planning, effective communication, and cross-functional collaboration.",
    "Question: How does Launch Excellence impact market success? Context: A successful launch can lead to increased market share, brand recognition, and revenue generation.",
    "Question: What tools and methodologies are used for Launch Excellence? Context: Project management tools, marketing automation platforms, and sales enablement tools are often used.",

    # Network Strategy and Bus.Dev Engineering
    "Question: What is the importance of network strategy in business development? Context: A strong network strategy can facilitate partnerships, access new markets, and drive business growth.",
    "Question: How does Bus.Dev Engineering contribute to network optimization? Context: Bus.Dev Engineering focuses on the technical aspects of network design, implementation, and maintenance.",
    "Question: What are the challenges in managing complex business networks? Context: Challenges include scalability, security, and interoperability.",

    # Capital Projects
    "Question: What are the different phases of a Capital Project? Context: Phases include initiation, planning, execution, monitoring and controlling, and closure.",
    "Question: How is risk managed in Capital Projects? Context: Risk management involves identifying, assessing, and mitigating potential risks throughout the project lifecycle.",
    "Question: What are the key stakeholders in Capital Projects? Context: Stakeholders include project sponsors, project managers, contractors, and end-users.",

    # Data Tools for Making Medicines
    "Question: What are the ethical considerations related to using data in medicine development? Context: Ethical considerations include data privacy, security, and bias in algorithms.",
    "Question: How can AI be used to accelerate drug discovery? Context: AI can be used to analyze large datasets, identify potential drug targets, and predict drug efficacy.",
    "Question: What are the challenges in integrating different data sources in medicine development? Context: Challenges include data standardization, data quality, and data security.",

    # Utilities Optimization
    "Question: What are some common areas for improvement in site utilities operations? Context: Areas for improvement include energy efficiency, water conservation, and waste reduction.",
    "Question: How can Communities of Practice (COPs) contribute to Utilities Optimization? Context: COPs provide a platform for sharing best practices, knowledge, and lessons learned.",
    "Question: What are the benefits of developing a utilities master plan? Context: A master plan provides a roadmap for long-term utilities infrastructure development and optimization.",

    # Compliance & Electrical Safety in Manufacturing
    "Question: What are the responsibilities of a Quality System Owner/SME for PQS? Context: Responsibilities include ensuring compliance with quality standards, managing documentation, and leading audits.",
    "Question: What is the purpose of site electrical program reviews? Context: Reviews ensure that electrical safety programs are effective and compliant with regulations.",
    "Question: What is the role of QCC representation in compliance and safety? Context: QCC (Quality Control Circle) representation promotes employee involvement in identifying and solving safety issues.",

    # Net Zero Strategic Initiative
    "Question: What are the key strategies for reducing site energy consumption? Context: Strategies include energy efficiency improvements, renewable energy sources, and behavioral changes.",
    "Question: How can digital tools like Enablon, EnPI, and Clockworks support Net Zero goals? Context: These tools can be used to track energy consumption, monitor emissions, and identify areas for improvement.",
    "Question: What are the benefits of achieving Net Zero emissions? Context: Benefits include reduced environmental impact, cost savings, and enhanced brand reputation.",

    # Cybersecurity in Manufacturing
    "Question: What are the common cybersecurity threats in manufacturing? Context: Threats include malware, ransomware, and denial-of-service attacks.",
    "Question: How can manufacturers protect their production systems from cyberattacks? Context: Measures include implementing firewalls, intrusion detection systems, and employee training programs.",
    "Question: What is the importance of incident response planning in manufacturing cybersecurity? Context: Incident response planning ensures that manufacturers can effectively respond to and recover from cyberattacks."
  ],
    "target_text": [
      # IMEx Ecosystem
      "The IMEx Ecosystem integrates various systems to optimize resource utilization and facilitate collaboration across facilities.",
      "IMEx improves resource utilization by providing real-time visibility into resource availability and enabling optimized allocation.",
      "IMEx fosters seamless collaboration by providing a centralized platform for information sharing and project management.",

      # Integrated Facilities Program (IFP)
      "The IFP is built on principles of standardization, efficiency, and continuous improvement in facilities management.",
      "The IFP contributes to cost savings by streamlining processes and optimizing resource allocation.",
      "KPIs for the IFP include operational efficiency, cost savings, and regulatory compliance.",

      # Compliance
      "Compliance includes adherence to environmental regulations, safety standards, and industry best practices.",
      "We ensure compliance with evolving regulations through regular audits, training, and updates on regulatory changes.",
      "Non-compliance can lead to penalties, reputational damage, and operational disruptions.",

      # Safety (Electrical Safety)
      "Common electrical hazards in a manufacturing environment include arc flash, electrical shock, and equipment malfunction.",
      "Safety measures in place to prevent electrical accidents include lockout/tagout procedures, regular equipment inspections, and employee training programs.",
      "PPE, such as insulated gloves and arc flash suits, provides an additional layer of protection against electrical hazards.",

      # Life Cycle Asset Management
      "The stages of Life Cycle Asset Management include planning, acquisition, operation, maintenance, and disposal.",
      "Life Cycle Asset Management impacts maintenance strategies by promoting proactive approaches to extend asset lifespan and minimize downtime.",
      "CMMS (Computerized Maintenance Management Systems) are commonly used tools for Life Cycle Asset Management.",

      # Capital Planning
      "Factors considered in Capital Planning include strategic goals, financial resources, risk assessment, and project prioritization.",
      "Capital Planning is aligned with business objectives by ensuring that investments support the long-term strategic direction of the organization.",
      "The approval process for Capital Projects typically involves review by a project committee and executive leadership.",

      # OpU Engineering
      "Key areas of focus for OpU Engineering include process optimization, cost reduction, and efficiency improvements.",
      "OpU Engineering contributes to operational excellence by applying engineering principles to drive continuous improvement and efficiency.",
      "Tools and techniques used in OpU Engineering include Lean manufacturing principles, Six Sigma methodologies, and data analytics.",

      # Environmental Engineering & Legacy Sites
      "Challenges associated with legacy site remediation include contamination assessment, remediation technology selection, and regulatory compliance.",
      "Environmental Engineering contributes to sustainability by remediating contaminated sites, helping protect the environment and human health.",
      "Various environmental regulations, specific to the location, govern legacy site management and remediation.",

      # Business Operation & Innovation
      "Businesses can foster a culture of innovation by encouraging experimentation, embracing new ideas, and providing resources for innovation.",
      "Different types of business innovation include product innovation, process innovation, and business model innovation.",
      "Businesses can measure the success of innovation initiatives using metrics such as revenue growth, market share, and customer satisfaction.",

      # Launch Excellence
      "Critical success factors for Launch Excellence include thorough planning, effective communication, and cross-functional collaboration.",
      "Launch Excellence impacts market success; a successful launch can lead to increased market share, brand recognition, and revenue generation.",
      "Tools and methodologies used for Launch Excellence include project management tools, marketing automation platforms, and sales enablement tools.",

      # Network Strategy and Bus.Dev Engineering
      "Network strategy is important in business development as it can facilitate partnerships, access new markets, and drive business growth.",
      "Bus.Dev Engineering contributes to network optimization by focusing on the technical aspects of network design, implementation, and maintenance.",
      "Challenges in managing complex business networks include scalability, security, and interoperability.",

      # Capital Projects
      "The different phases of a Capital Project include initiation, planning, execution, monitoring and controlling, and closure.",
      "Risk is managed in Capital Projects by identifying, assessing, and mitigating potential risks throughout the project lifecycle.",
      "Key stakeholders in Capital Projects include project sponsors, project managers, contractors, and end-users.",

      # Data Tools for Making Medicines
      "Ethical considerations related to using data in medicine development include data privacy, security, and bias in algorithms.",
      "AI can be used to accelerate drug discovery by analyzing large datasets, identifying potential drug targets, and predicting drug efficacy.",
      "Challenges in integrating different data sources in medicine development include data standardization, data quality, and data security.",

      # Utilities Optimization
      "Common areas for improvement in site utilities operations include energy efficiency, water conservation, and waste reduction.",
      "Communities of Practice (COPs) can contribute to Utilities Optimization by providing a platform for sharing best practices, knowledge, and lessons learned.",
      "The benefits of developing a utilities master plan include providing a roadmap for long-term utilities infrastructure development and optimization.",

      # Compliance & Electrical Safety in Manufacturing
      "Responsibilities of a Quality System Owner/SME for PQS include ensuring compliance with quality standards, managing documentation, and leading audits.",
      "The purpose of site electrical program reviews is to ensure that electrical safety programs are effective and compliant with regulations.",
      "QCC (Quality Control Circle) representation in compliance and safety promotes employee involvement in identifying and solving safety issues.",

      # Net Zero Strategic Initiative
      "Key strategies for reducing site energy consumption include energy efficiency improvements, renewable energy sources, and behavioral changes.",
      "Digital tools like Enablon, EnPI, and Clockworks can support Net Zero goals by tracking energy consumption, monitoring emissions, and identifying areas for improvement.",
      "The benefits of achieving Net Zero emissions include reduced environmental impact, cost savings, and enhanced brand reputation.",

      # Cybersecurity in Manufacturing
      "Common cybersecurity threats in manufacturing include malware, ransomware, and denial-of-service attacks.",
      "Manufacturers can protect their production systems from cyberattacks by implementing firewalls, intrusion detection systems, and employee training programs.",
      "Incident response planning is important in manufacturing cybersecurity to ensure that manufacturers can effectively respond to and recover from cyberattacks."
  ]
}

if __name__ == "__main__":
    # For quick inspection: print out each Q&A pair.
    for inp, tgt in zip(training_data["input_text"], training_data["target_text"]):
        print(f"Input: {inp}\nTarget: {tgt}\n")
