# Savings Goal Tracking System - Pseudocode
# Financial Technology Company - Mobile Banking App Feature

"""
REQUIREMENTS ANALYSIS:

Main Functionalities:
1. Savings Goal Management
2. Savings Progress Tracking  
3. Savings Goal Status Monitoring
4. Savings Goal Notification System

Variables:
- User ID (string/integer)
- Target Amount (decimal/float)
- Target Date (date)
- Savings Goal ID (string/integer)
- Amount Saved (decimal/float)
- Goal Name (string)
- Creation Date (date)

Actions: Create, Store, Return, Update, Retrieve, Compose, Send
"""

# PSEUDOCODE FOR SAVINGS GOAL TRACKING SYSTEM

# ===== DATA STRUCTURES =====
ALGORITHM InitializeDataStructures
BEGIN
    CREATE SavingsGoals as empty dictionary
    CREATE UserNotifications as empty list
    CREATE CurrentDate as system date
END

# ===== SAVINGS GOAL MANAGEMENT =====
ALGORITHM CreateSavingsGoal
INPUT: userID, goalName, targetAmount, targetDate
BEGIN
    CREATE goalID as unique identifier
    CREATE newGoal with:
        - goalID
        - userID  
        - goalName
        - targetAmount
        - targetDate
        - amountSaved = 0
        - creationDate = CurrentDate
        - status = "Active"
    
    STORE newGoal in SavingsGoals[goalID]
    RETURN goalID
END

ALGORITHM RetrieveSavingsGoal
INPUT: goalID
BEGIN
    IF goalID exists in SavingsGoals THEN
        RETURN SavingsGoals[goalID]
    ELSE
        RETURN "Goal not found"
    END IF
END

# ===== SAVINGS PROGRESS TRACKING =====
ALGORITHM UpdateSavingsProgress
INPUT: goalID, additionalAmount
BEGIN
    RETRIEVE goal from SavingsGoals[goalID]
    IF goal exists THEN
        UPDATE goal.amountSaved = goal.amountSaved + additionalAmount
        
        IF goal.amountSaved >= goal.targetAmount THEN
            UPDATE goal.status = "Completed"
            CALL SendGoalCompletedNotification(goal)
        END IF
        
        STORE updated goal in SavingsGoals[goalID]
        RETURN "Progress updated successfully"
    ELSE
        RETURN "Goal not found"
    END IF
END

ALGORITHM CalculateProgressPercentage
INPUT: goalID
BEGIN
    RETRIEVE goal from SavingsGoals[goalID]
    IF goal exists THEN
        SET percentage = (goal.amountSaved / goal.targetAmount) * 100
        RETURN percentage
    ELSE
        RETURN 0
    END IF
END

# ===== SAVINGS GOAL STATUS MONITORING =====
ALGORITHM CheckGoalStatus
INPUT: goalID
BEGIN
    RETRIEVE goal from SavingsGoals[goalID]
    IF goal exists THEN
        SET daysRemaining = goal.targetDate - CurrentDate
        SET progressPercentage = CalculateProgressPercentage(goalID)
        
        IF goal.amountSaved >= goal.targetAmount THEN
            RETURN "Completed"
        ELSE IF daysRemaining <= 0 THEN
            RETURN "Overdue"
        ELSE IF daysRemaining <= 7 AND progressPercentage < 80 THEN
            RETURN "At Risk"
        ELSE
            RETURN "On Track"
        END IF
    ELSE
        RETURN "Goal not found"
    END IF
END

# ===== NOTIFICATION SYSTEM =====
ALGORITHM CheckApproachingDeadlines
BEGIN
    FOR each goal in SavingsGoals DO
        SET daysRemaining = goal.targetDate - CurrentDate
        SET progressPercentage = CalculateProgressPercentage(goal.goalID)
        
        IF daysRemaining <= 7 AND goal.status = "Active" AND progressPercentage < 100 THEN
            CALL ComposeDeadlineWarning(goal)
        END IF
    END FOR
END

ALGORITHM ComposeDeadlineWarning
INPUT: goal
BEGIN
    SET message = "Your savings goal '" + goal.goalName + "' is approaching its deadline. "
    SET message = message + "You have " + daysRemaining + " days left and need $"
    SET remainingAmount = goal.targetAmount - goal.amountSaved
    SET message = message + remainingAmount + " more to reach your goal."
    
    CALL SendNotification(goal.userID, message)
END

ALGORITHM SendNotification
INPUT: userID, message
BEGIN
    CREATE notification with:
        - userID
        - message
        - timestamp = CurrentDate
        - type = "Goal Reminder"
    
    STORE notification in UserNotifications
    SEND push notification to user device
    RETURN "Notification sent successfully"
END

ALGORITHM SendGoalCompletedNotification
INPUT: goal
BEGIN
    SET message = "Congratulations! You've reached your savings goal: " + goal.goalName
    CALL SendNotification(goal.userID, message)
END

# ===== USER INTERFACE FUNCTIONS =====
ALGORITHM GetUserGoals
INPUT: userID
BEGIN
    CREATE userGoals as empty list
    FOR each goal in SavingsGoals DO
        IF goal.userID = userID THEN
            ADD goal to userGoals
        END IF
    END FOR
    RETURN userGoals
END

ALGORITHM GetGoalSummary
INPUT: goalID
BEGIN
    RETRIEVE goal from SavingsGoals[goalID]
    IF goal exists THEN
        SET summary with:
            - goalName = goal.goalName
            - targetAmount = goal.targetAmount
            - amountSaved = goal.amountSaved
            - progressPercentage = CalculateProgressPercentage(goalID)
            - daysRemaining = goal.targetDate - CurrentDate
            - status = CheckGoalStatus(goalID)
        
        RETURN summary
    ELSE
        RETURN "Goal not found"
    END IF
END

# ===== MAIN SYSTEM WORKFLOW =====
ALGORITHM MainSavingsGoalSystem
BEGIN
    CALL InitializeDataStructures()
    
    WHILE system is running DO
        CALL CheckApproachingDeadlines()
        
        WAIT for user action:
            CASE "Create Goal":
                INPUT userID, goalName, targetAmount, targetDate
                CALL CreateSavingsGoal(userID, goalName, targetAmount, targetDate)
            
            CASE "Update Progress":
                INPUT goalID, additionalAmount
                CALL UpdateSavingsProgress(goalID, additionalAmount)
            
            CASE "Check Status":
                INPUT goalID
                CALL GetGoalSummary(goalID)
            
            CASE "View My Goals":
                INPUT userID
                CALL GetUserGoals(userID)
        END CASE
    END WHILE
END