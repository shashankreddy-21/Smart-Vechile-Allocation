
from dataclasses import dataclass
import heapq

# ==========================================================
# CO1: State Representation using Dataclasses
# ==========================================================

@dataclass
class ParkingSlot:
    slot_id: str
    distance: int
    slot_type: str
    occupied: bool = False
    availability_prob: float = 1.0


@dataclass
class Vehicle:
    vehicle_no: str
    vehicle_type: str


# ==========================================================
# SMART PARKING SYSTEM
# ==========================================================

class SmartParkingSystem:

    def __init__(self):

        # CO1: Knowledge Representation using Objects and Lists

        self.slots = [
            ParkingSlot("A1", 2, "Car", False, 0.95),
            ParkingSlot("A2", 5, "Car", False, 0.80),
            ParkingSlot("A3", 8, "Car", False, 0.70),
            ParkingSlot("B1", 1, "Bike", False, 0.90),
            ParkingSlot("B2", 4, "Bike", False, 0.85),
            ParkingSlot("B3", 7, "Bike", False, 0.75)
        ]

    # ======================================================
    # CO3: CSP Constraint Checking
    # ======================================================

    def is_valid_slot(self, vehicle, slot):

        if slot.occupied:
            print(f"{slot.slot_id} Rejected -> Slot Occupied")
            return False

        if vehicle.vehicle_type.lower() != slot.slot_type.lower():
            print(f"{slot.slot_id} Rejected -> Vehicle Type Mismatch")
            return False

        return True

    # ======================================================
    # CO2: A* Style Search
    # ======================================================

    def find_best_slot(self, vehicle):

        open_list = []

        print("\nSearching Available Slots...\n")

        for slot in self.slots:

            if self.is_valid_slot(vehicle, slot):

                # CO5: Probability Reasoning

                heuristic = 1 - slot.availability_prob

                # CO2: f(n)=g(n)+h(n)

                cost = slot.distance + heuristic

                print(
                    f"Slot={slot.slot_id} | "
                    f"Distance={slot.distance} | "
                    f"Probability={slot.availability_prob} | "
                    f"Cost={cost:.2f}"
                )

                heapq.heappush(
                    open_list,
                    (cost, slot.slot_id, slot)
                )

        if not open_list:
            return None

        return heapq.heappop(open_list)[2]

    # ======================================================
    # CO4: Utility Function
    # ======================================================

    def calculate_utility(self, slot):

        return (10 - slot.distance) * slot.availability_prob

    # ======================================================
    # CO6: Hybrid AI System
    #
    # Combines:
    # Search + CSP + Probability + Utility
    # ======================================================

    def allocate_slot(self, vehicle):

        if vehicle.vehicle_no.strip() == "":
            print("Vehicle Number Cannot Be Empty")
            return

        slot = self.find_best_slot(vehicle)

        if slot is None:
            print("\nNo Suitable Slot Found")
            return

        utility = self.calculate_utility(slot)

        print("\n========== REASONING TRACE ==========")
        print("Vehicle Number      :", vehicle.vehicle_no)
        print("Vehicle Type        :", vehicle.vehicle_type)
        print("Selected Slot       :", slot.slot_id)
        print("Distance            :", slot.distance)
        print("Availability Prob.  :", slot.availability_prob)
        print("Utility Score       :", round(utility, 2))
        print("=====================================")

        slot.occupied = True

        print("\nParking Allocated Successfully!")

    # ======================================================
    # CO1: State Update
    # ======================================================

    def release_slot(self, slot_id):

        for slot in self.slots:

            if slot.slot_id.upper() == slot_id.upper():

                if slot.occupied:
                    slot.occupied = False
                    print("Slot Released Successfully")
                else:
                    print("Slot Already Free")

                return

        print("Invalid Slot ID")

    # ======================================================
    # CO1 & CO6: Search Feature
    # ======================================================

    def search_slot(self, slot_id):

        for slot in self.slots:

            if slot.slot_id.upper() == slot_id.upper():

                print("\n====== SLOT DETAILS ======")
                print("Slot ID      :", slot.slot_id)
                print("Type         :", slot.slot_type)
                print("Distance     :", slot.distance)
                print("Occupied     :", slot.occupied)
                print("Probability  :", slot.availability_prob)
                print("==========================")

                return

        print("Slot Not Found")

    # ======================================================
    # CO1 & CO6: Edit Feature
    # ======================================================

    def edit_slot(self, slot_id):

        for slot in self.slots:

            if slot.slot_id.upper() == slot_id.upper():

                print("\nCurrent Details")
                print("Distance    :", slot.distance)
                print("Probability :", slot.availability_prob)

                try:

                    new_distance = int(
                        input("Enter New Distance: ")
                    )

                    new_probability = float(
                        input("Enter New Probability (0-1): ")
                    )

                    slot.distance = new_distance
                    slot.availability_prob = new_probability

                    print("Slot Updated Successfully")

                except ValueError:

                    print("Invalid Input")

                return

        print("Slot Not Found")

    # ======================================================
    # CO1: Display Current Environment State
    # ======================================================

    def display_slots(self):

        print("\n========== PARKING STATUS ==========")
        print("Slot\tType\tDistance\tStatus")

        for slot in self.slots:

            status = "Occupied" if slot.occupied else "Free"

            print(
                f"{slot.slot_id}\t"
                f"{slot.slot_type}\t"
                f"{slot.distance}\t\t"
                f"{status}"
            )

        print("====================================")


# ==========================================================
# CO1: PEAS MODEL
# ==========================================================

def main():

    parking_system = SmartParkingSystem()

    while True:

        print("\n===================================")
        print(" SMART PARKING ALLOCATION SYSTEM ")
        print("===================================")
        print("1. View Parking Slots")
        print("2. Allocate Parking")
        print("3. Release Slot")
        print("4. Search Slot")
        print("5. Edit Slot")
        print("6. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            parking_system.display_slots()

        elif choice == "2":

            vehicle_no = input("Enter Vehicle Number: ")
            vehicle_type = input("Enter Vehicle Type (Car/Bike): ")

            vehicle = Vehicle(vehicle_no, vehicle_type)

            parking_system.allocate_slot(vehicle)

        elif choice == "3":

            slot_id = input("Enter Slot ID to Release: ")

            parking_system.release_slot(slot_id)

        elif choice == "4":

            slot_id = input("Enter Slot ID to Search: ")

            parking_system.search_slot(slot_id)

        elif choice == "5":

            slot_id = input("Enter Slot ID to Edit: ")

            parking_system.edit_slot(slot_id)

        elif choice == "6":

            print("\nThank You!")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()
