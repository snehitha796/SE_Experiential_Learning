# Lab 1: Requirements Engineering & UML Use-Case Modelling

## Student Club Event Ticketing & Budget Portal

### 1. Project Overview

The **Student Club Event Ticketing & Budget Portal** is an integrated system designed to support student clubs in managing event proposals, university budget allocation requests, and event ticketing.

The system provides a structured workflow in which club event proposals can be submitted and reviewed, budget requests can be processed through the appropriate approval workflow, and QR-code tickets can be generated and validated for event attendees.

### 2. Problem Context

Student clubs require a centralized portal to manage the process of organizing events. The system is intended to simplify event proposal submission, university approval, budget allocation, and attendee ticket management while ensuring that access to sensitive functions is controlled according to user roles.

### 3. Actors

The following actors interact with the system:

* **Club Lead** – Submits event proposals, requests budget allocations, and manages event tickets.
* **Campus Admin** – Reviews and approves or rejects student club event proposals.
* **Finance Officer** – Reviews and approves or rejects budget allocation requests.
* **Attendee** – Uses a QR-code ticket for event entry and check-in.

### 4. Functional Requirements

The project specifies exactly five Functional Requirements:

| Req ID | Requirement                      |
| ------ | -------------------------------- |
| FR-001 | Submit Event Proposal            |
| FR-002 | Request Budget Allocation        |
| FR-003 | Approve or Reject Event Proposal |
| FR-004 | Approve or Reject Budget Request |
| FR-005 | Generate QR-Code Tickets         |

Each functional requirement includes its description, priority, measurable acceptance criteria, and rationale in the Requirements document.

### 5. Non-Functional Requirements

The project specifies two Non-Functional Requirements:

| Req ID  | Requirement |
| ------- | ----------- |
| NFR-001 | Performance |
| NFR-002 | Security    |

The non-functional requirements define measurable performance and role-based access-control expectations for the system.

### 6. UML Use Cases

The UML Use-Case Diagram contains the following use cases:

* **UC-01 – Submit Event Proposal**
* **UC-02 – Request Budget Allocation**
* **UC-03 – Review Event Proposal**
* **UC-04 – Review Budget Request**
* **UC-05 – Generate QR-Code Tickets**
* **UC-06 – Check In Attendee**
* **UC-07 – Validate QR Ticket**
* **UC-08 – Regenerate QR Ticket**

### 7. UML Relationships

The UML Use-Case Diagram includes both required relationship types.

#### `<<include>>` Relationship

**UC-06 – Check In Attendee** `<<include>>` **UC-07 – Validate QR Ticket**

QR-ticket validation is a required part of the attendee check-in process. Therefore, the Check In Attendee use case includes Validate QR Ticket.

#### `<<extend>>` Relationship

**UC-08 – Regenerate QR Ticket** `<<extend>>` **UC-05 – Generate QR-Code Tickets**

Regenerating a QR ticket represents optional or conditional behaviour that occurs when an existing ticket needs to be regenerated.

### 8. Use-Case Flow

The detailed Use-Case Flow is specified for:

**UC-06 – Check In Attendee**

The flow contains:

* Preconditions
* Main Success Scenario
* Alternate Flow for an invalid or expired QR ticket
* Alternate Flow for an already-used ticket
* Postconditions

The main success scenario describes the normal QR-ticket check-in process, while the alternate flows describe how the system handles unsuccessful check-in conditions.

### 9. Project Files

The repository contains the following deliverables:

| File                       | Description                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `README.md`                | Project overview, actors, requirements, use cases, relationships, and deliverables                          |
| `Requirements.docx`        | Requirements Table containing 5 Functional Requirements and 2 Non-Functional Requirements                   |
| `Use_Case_Flow.docx`       | Use-Case Flow Specification for UC-06 – Check In Attendee                                                   |
| `UML_Use_Case_Diagram.pdf` | UML Use-Case Diagram showing actors, use cases, associations, `<<include>>`, and `<<extend>>` relationships |

### 10. Tools Used

* **Microsoft Word** – Requirements Table and Use-Case Flow
* **draw.io / diagrams.net** – UML Use-Case Diagram
* **GitHub** – Repository management and submission

### 11. Lab Deliverables

This repository contains the deliverables for **Lab 1: Requirements Engineering & UML Use-Case Modelling**:

1. A Requirements Table containing exactly **5 Functional Requirements** and **2 Non-Functional Requirements**.
2. A UML Use-Case Diagram containing the identified actors and use cases, along with associations, `<<include>>`, and `<<extend>>` relationships.
3. A Use-Case Flow Specification for **UC-06 – Check In Attendee**, including the Main Success Scenario and Alternate Flows.
4. This README file documenting the project and its contents.
