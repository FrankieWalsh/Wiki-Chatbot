import json

# Training data covering the specified topics and keywords.
training_data = {
  "input_text": [
    # IMEx Ecosystem
    "Question: What are the key components of the IMEx Ecosystem? Context: The IMEx Ecosystem comprises interconnected systems, including data management platforms, collaboration tools, and resource allocation systems.",
    "Question: How does the IMEx Ecosystem improve resource utilization? Context: By integrating various systems, IMEx enables real-time visibility into resource availability and facilitates optimized allocation.",
    "Question: What are the benefits of the IMEx Ecosystem for collaboration? Context: IMEx fosters seamless collaboration by providing a centralized platform for information sharing and project management.",
    "Question: How does the IMEx Ecosystem handle data security and privacy? Context: IMEx incorporates robust security measures to protect sensitive data and ensure compliance with privacy regulations.",
    "Question: Can the IMEx Ecosystem be customized to meet specific business needs? Context: Yes, IMEx is designed to be flexible and customizable to accommodate unique organizational requirements.",
    "Question: What training and support are available for users of the IMEx Ecosystem? Context: Comprehensive training programs and ongoing support are provided to ensure users can effectively utilize IMEx's capabilities.",

    # Integrated Facilities Program (IFP)
    "Question: What are the core principles of the IFP? Context: The IFP is built on principles of standardization, efficiency, and continuous improvement in facilities management.",
    "Question: How does the IFP contribute to cost savings? Context: By streamlining processes and optimizing resource allocation, the IFP helps reduce operational costs.",
    "Question: What are the key performance indicators (KPIs) for the IFP? Context: KPIs for the IFP include operational efficiency, cost savings, and regulatory compliance.",
    "Question: How does the IFP address sustainability in facilities management? Context: The IFP promotes sustainable practices through energy efficiency initiatives, waste reduction programs, and environmentally friendly procurement.",
    "Question: What are the challenges in implementing the IFP across a large organization? Context: Implementing the IFP can be challenging due to variations in site infrastructure, processes, and organizational culture.",
    "Question: How does the IFP integrate with other business systems? Context: The IFP is designed to integrate with other relevant business systems, such as finance, HR, and procurement, to ensure seamless data flow.",

    # Compliance
    "Question: What are the different types of compliance relevant to our operations? Context: Compliance includes adherence to environmental regulations, safety standards, and industry best practices.",
    "Question: How do we ensure compliance with evolving regulations? Context: We maintain a robust compliance program that includes regular audits, training, and updates on regulatory changes.",
    "Question: What are the consequences of non-compliance? Context: Non-compliance can lead to penalties, reputational damage, and operational disruptions.",
    "Question: What are the key elements of an effective compliance program? Context: An effective compliance program includes policies and procedures, training, monitoring, reporting, and enforcement.",
    "Question: How do we stay informed about changes in regulations? Context: We subscribe to regulatory updates, participate in industry events, and work closely with legal experts to stay informed.",
    "Question: How do we handle compliance violations? Context: We have a clear process for reporting, investigating, and addressing compliance violations, including disciplinary actions when necessary.",


    # Safety (Electrical Safety)
    "Question: What are the common electrical hazards in a manufacturing environment? Context: Common hazards include arc flash, electrical shock, and equipment malfunction.",
    "Question: What safety measures are in place to prevent electrical accidents? Context: We have implemented lockout/tagout procedures, regular equipment inspections, and employee training programs.",
    "Question: What is the role of personal protective equipment (PPE) in electrical safety? Context: PPE, such as insulated gloves and arc flash suits, provides an additional layer of protection against electrical hazards.",
    "Question: What are the different types of electrical protective devices? Context: Electrical protective devices include circuit breakers, fuses, and ground fault circuit interrupters (GFCI).",
    "Question: How often should electrical equipment be inspected? Context: Electrical equipment should be inspected regularly, with the frequency depending on the type of equipment and the environment it operates in.",
    "Question: What is arc flash and how can it be prevented? Context: Arc flash is a dangerous electrical explosion that can cause severe burns. It can be prevented through proper equipment maintenance, safe work practices, and the use of arc-rated PPE.",


    # Life Cycle Asset Management
    "Question: What are the stages of Life Cycle Asset Management? Context: The stages include planning, acquisition, operation, maintenance, and disposal.",
    "Question: How does Life Cycle Asset Management impact maintenance strategies? Context: It promotes proactive maintenance strategies to extend asset lifespan and minimize downtime.",
    "Question: What tools are used for Life Cycle Asset Management? Context: CMMS (Computerized Maintenance Management Systems) are commonly used to track and manage assets.",
    "Question: What are the benefits of implementing a proactive maintenance strategy? Context: Proactive maintenance reduces downtime, extends asset lifespan, and improves overall operational efficiency.",
    "Question: How does Life Cycle Asset Management contribute to cost optimization? Context: By optimizing maintenance schedules and minimizing unplanned downtime, Life Cycle Asset Management helps reduce costs.",
    "Question: What are some best practices for asset disposal? Context: Best practices for asset disposal include proper decommissioning, recycling or reuse of materials, and compliance with environmental regulations.",


    # Capital Planning
    "Question: What factors are considered in Capital Planning? Context: Factors include strategic goals, financial resources, risk assessment, and project prioritization.",
    "Question: How is Capital Planning aligned with business objectives? Context: Capital Planning ensures that investments support the long-term strategic direction of the organization.",
    "Question: What is the process for approving Capital Projects? Context: The approval process typically involves review by a project committee and executive leadership.",
    "Question: What is the role of risk assessment in Capital Planning? Context: Risk assessment helps identify potential risks and develop mitigation strategies to ensure project success.",
    "Question: How are Capital Projects prioritized? Context: Capital Projects are typically prioritized based on their strategic importance, financial return, and alignment with business objectives.",
    "Question: What is the importance of stakeholder engagement in Capital Planning? Context: Stakeholder engagement ensures that the needs and expectations of all relevant parties are considered in the planning process.",


    # OpU Engineering
    "Question: What are the key areas of focus for OpU Engineering? Context: OpU Engineering focuses on process optimization, cost reduction, and efficiency improvements.",
    "Question: How does OpU Engineering contribute to operational excellence? Context: By applying engineering principles, OpU Engineering drives continuous improvement and operational efficiency.",
    "Question: What tools and techniques are used in OpU Engineering? Context: Lean manufacturing principles, Six Sigma methodologies, and data analytics are commonly used.",
    "Question: How does OpU Engineering support continuous improvement initiatives? Context: OpU Engineering provides the tools and methodologies for identifying areas for improvement, implementing changes, and tracking results.",
    "Question: What is the role of data analytics in OpU Engineering? Context: Data analytics is used to identify trends, patterns, and insights that can inform operational decisions and drive improvements.",
    "Question: How does OpU Engineering collaborate with other departments? Context: OpU Engineering works closely with other departments, such as maintenance, production, and quality, to ensure that operational improvements are aligned with overall business goals.",

    # Environmental Engineering & Legacy Sites
    "Question: What are the challenges associated with legacy site remediation? Context: Challenges include contamination assessment, remediation technology selection, and regulatory compliance.",
    "Question: How does Environmental Engineering contribute to sustainability? Context: By remediating contaminated sites, Environmental Engineering helps protect the environment and human health.",
    "Question: What regulations govern legacy site management? Context: Various environmental regulations, specific to the location, govern legacy site management and remediation. ",
    "Question: What are some common remediation techniques for contaminated sites? Context: Common remediation techniques include excavation and disposal, soil washing, and bioremediation.",
    "Question: How is the effectiveness of remediation efforts measured? Context: The effectiveness of remediation efforts is measured through regular monitoring and testing to ensure that contamination levels are reduced to acceptable levels.",
    "Question: What is the long-term management plan for legacy sites? Context: A long-term management plan outlines the ongoing monitoring, maintenance, and any necessary further remediation activities for a legacy site.",

    # Business Operation & Innovation
    "Question: How can businesses foster a culture of innovation? Context: By encouraging experimentation, embracing new ideas, and providing resources for innovation.",
    "Question: What are the different types of business innovation? Context: Innovation can include product innovation, process innovation, and business model innovation.",
    "Question: How can businesses measure the success of innovation initiatives? Context: Metrics such as revenue growth, market share, and customer satisfaction can be used.",
    "Question: How can businesses encourage employee participation in innovation? Context: Businesses can encourage employee participation through suggestion programs, innovation challenges, and cross-functional teams.",
    "Question: What is the role of leadership in fostering a culture of innovation? Context: Leaders play a crucial role in setting the tone for innovation, providing resources, and recognizing and rewarding innovative ideas.",
    "Question: How can businesses protect their intellectual property related to innovation? Context: Businesses can protect their intellectual property through patents, trademarks, copyrights, and trade secrets.",

    # Launch Excellence
    "Question: What are the critical success factors for Launch Excellence? Context: Critical factors include thorough planning, effective communication, and cross-functional collaboration.",
    "Question: How does Launch Excellence impact market success? Context: A successful launch can lead to increased market share, brand recognition, and revenue generation.",
    "Question: What tools and methodologies are used for Launch Excellence? Context: Project management tools, marketing automation platforms, and sales enablement tools are often used.",
    "Question: What are the key activities involved in a product launch? Context: Key activities include market research, product development, marketing and communication, sales training, and customer support.",
    "Question: How can businesses measure the success of a product launch? Context: Businesses can measure the success of a product launch through metrics such as sales revenue, market share, customer adoption, and brand awareness.",
    "Question: What are some common challenges in product launches? Context: Common challenges include delays in development, unexpected competition, and difficulty in reaching target customers.",

    # Network Strategy and Bus.Dev Engineering
    "Question: What is the importance of network strategy in business development? Context: A strong network strategy can facilitate partnerships, access new markets, and drive business growth.",
    "Question: How does Bus.Dev Engineering contribute to network optimization? Context: Bus.Dev Engineering focuses on the technical aspects of network design, implementation, and maintenance.",
    "Question: What are the challenges in managing complex business networks? Context: Challenges include scalability, security, and interoperability.",
    "Question: What are the different types of business networks? Context: Different types of business networks include supply chain networks, distribution networks, and strategic alliances.",
    "Question: How can businesses identify potential partners for network expansion? Context: Businesses can identify potential partners through industry events, online platforms, and referrals.",
    "Question: What are the key considerations in negotiating partnerships? Context: Key considerations include mutual benefit, shared goals, trust, and clear contractual agreements.",

    # Capital Projects
    "Question: What are the different phases of a Capital Project? Context: Phases include initiation, planning, execution, monitoring and controlling, and closure.",
    "Question: How is risk managed in Capital Projects? Context: Risk management involves identifying, assessing, and mitigating potential risks throughout the project lifecycle.",
    "Question: What are the key stakeholders in Capital Projects? Context: Stakeholders include project sponsors, project managers, contractors, and end-users.",
    "Question: What are the different types of Capital Projects? Context: Capital Projects can include infrastructure projects, equipment upgrades, facility expansions, and technology implementations.",
    "Question: How is project progress monitored and controlled? Context: Project progress is monitored through regular meetings, progress reports, and performance tracking against the project plan.",
    "Question: What is the process for closing out a Capital Project? Context: The project closeout process involves final inspections, documentation, financial reconciliation, and handover to operations.",

    # Data Tools for Making Medicines
    "Question: What are the ethical considerations related to using data in medicine development? Context: Ethical considerations include data privacy, security, and bias in algorithms.",
    "Question: How can AI be used to accelerate drug discovery? Context: AI can be used to analyze large datasets, identify potential drug targets, and predict drug efficacy.",
    "Question: What are the challenges in integrating different data sources in medicine development? Context: Challenges include data standardization, data quality, and data security.",
    "Question: What are some examples of advanced sensors used in medicine manufacturing? Context: Examples include biosensors, chemical sensors, and environmental sensors.",
    "Question: How can machine learning be used to optimize medicine production processes? Context: Machine learning can be used to analyze data from production processes to identify areas for improvement, predict equipment failures, and optimize process parameters.",
    "Question: What are the regulatory requirements for data integrity in medicine manufacturing? Context: Regulatory requirements for data integrity include ensuring data accuracy, completeness, consistency, and traceability.",

    # Utilities Optimization
    "Question: What are some common areas for improvement in site utilities operations? Context: Areas for improvement include energy efficiency, water conservation, and waste reduction.",
    "Question: How can Communities of Practice (COPs) contribute to Utilities Optimization? Context: COPs provide a platform for sharing best practices, knowledge, and lessons learned.",
    "Question: What are the benefits of developing a utilities master plan? Context: A master plan provides a roadmap for long-term utilities infrastructure development and optimization.",
    "Question: What are some common energy efficiency measures in site utilities operations? Context: Common measures include upgrading to energy-efficient equipment, optimizing HVAC systems, and reducing lighting loads.",
    "Question: How can water consumption be reduced in site utilities operations? Context: Water consumption can be reduced through leak detection and repair, water-efficient landscaping, and process optimization.",
    "Question: What are the benefits of participating in Communities of Practice (COPs)? Context: Participating in COPs allows individuals to share best practices, learn from others' experiences, and stay up-to-date on industry trends.",

    # Compliance & Electrical Safety in Manufacturing
    "Question: What are the responsibilities of a Quality System Owner/SME for PQS? Context: Responsibilities include ensuring compliance with quality standards, managing documentation, and leading audits.",
    "Question: What is the purpose of site electrical program reviews? Context: Reviews ensure that electrical safety programs are effective and compliant with regulations.",
    "Question: What is the role of QCC representation in compliance and safety? Context: QCC (Quality Control Circle) representation promotes employee involvement in identifying and solving safety issues.",
    "Question: What are the different types of electrical hazards in the workplace? Context: Electrical hazards include shock, arc flash, arc blast, and burns.",
    "Question: How can electrical safety training be made more effective? Context: Electrical safety training can be made more effective through hands-on training, real-life case studies, and regular refreshers.",
    "Question: What are the responsibilities of employees in maintaining electrical safety? Context: Employees are responsible for following safe work practices, reporting electrical hazards, and using electrical equipment properly.",

    # Net Zero Strategic Initiative
    "Question: What are the key strategies for reducing site energy consumption? Context: Strategies include energy efficiency improvements, renewable energy sources, and behavioral changes.",
    "Question: How can digital tools like Enablon, EnPI, and Clockworks support Net Zero goals? Context: These tools can be used to track energy consumption, monitor emissions, and identify areas for improvement.",
    "Question: What are the benefits of achieving Net Zero emissions? Context: Benefits include reduced environmental impact, cost savings, and enhanced brand reputation.",
    "Question: What are some examples of renewable energy sources that can be used in manufacturing facilities? Context: Examples include solar power, wind power, and geothermal energy.",
    "Question: How can behavioral changes contribute to Net Zero goals? Context: Behavioral changes, such as turning off lights when not in use and reducing energy consumption during off-peak hours, can make a significant difference.",
    "Question: What are the financial incentives for achieving Net Zero emissions? Context: Financial incentives can include tax credits, rebates, and grants for renewable energy projects and energy efficiency improvements.",

    # Cybersecurity in Manufacturing
    "Question: What are the common cybersecurity threats in manufacturing? Context: Threats include malware, ransomware, and denial-of-service attacks.",
    "Question: How can manufacturers protect their production systems from cyberattacks? Context: Measures include implementing firewalls, intrusion detection systems, and employee training programs.",
    "Question: What is the importance of incident response planning in manufacturing cybersecurity? Context: Incident response planning ensures that manufacturers can effectively respond to and recover from cyberattacks."
    "Question: What is the role of network segmentation in manufacturing cybersecurity? Context: Network segmentation helps isolate critical production systems from other networks, limiting the impact of a cyberattack.",
    "Question: How can manufacturers protect against insider threats? Context: Manufacturers can protect against insider threats through background checks, access controls, and monitoring of employee activity.",
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
