# Savings Goal Tracking System - Design Summary

## Requirements Analysis

### Main Functionalities
1. **Savings Goal Management** - Create and store new savings goals
2. **Savings Progress Tracking** - Update and monitor progress toward goals  
3. **Savings Goal Status Monitoring** - Check current status and calculate progress
4. **Savings Goal Notification System** - Alert users about approaching deadlines

### Key Variables
- **User ID** - Unique identifier for each user
- **Target Amount** - Financial goal amount to be saved
- **Target Date** - Deadline for achieving the savings goal
- **Savings Goal ID** - Unique identifier for each goal
- **Amount Saved** - Current progress toward the target amount
- **Goal Name** - User-friendly name for the savings goal
- **Creation Date** - When the goal was established

### System Actions
- **Create** - Establish new savings goals
- **Store** - Persist goal data in system
- **Return** - Provide data back to user interface
- **Update** - Modify existing goal progress
- **Retrieve** - Fetch stored goal information
- **Compose** - Generate notification messages
- **Send** - Deliver notifications to users

## Input/Output Requirements

### Create Savings Goal
- **Input**: User ID, Goal Name, Target Amount, Target Date
- **Output**: Goal ID, Success/Error message

### Update Progress
- **Input**: Goal ID, Additional Amount
- **Output**: Updated progress, Success/Error message, Completion notification (if applicable)

### Check Status
- **Input**: Goal ID
- **Output**: Goal summary with progress percentage, days remaining, current status

### Notification System
- **Input**: System-triggered based on dates and progress
- **Output**: Push notifications, warning messages

## Algorithm Design Principles

1. **Modular Design** - Each functionality is separated into distinct algorithms
2. **Error Handling** - Validation for goal existence and data integrity
3. **Automated Monitoring** - Background process for deadline checking
4. **User-Centric** - Clear feedback and progress tracking
5. **Scalable** - Dictionary-based storage allows for multiple users and goals

## Key Features

- **Progress Calculation** - Automatic percentage calculation
- **Status Classification** - Goals categorized as Completed, Overdue, At Risk, or On Track
- **Proactive Notifications** - 7-day warning system for approaching deadlines
- **Multi-User Support** - System handles multiple users with separate goal tracking
- **Real-Time Updates** - Immediate feedback on progress changes

This pseudocode provides a comprehensive foundation for implementing the savings goal tracking feature in the mobile banking application.