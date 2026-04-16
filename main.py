import event
import person
def main():
    john = person.Person(
        "John Doe",
        30,
        events={
            0: event.Event("enter", {"location": "Kitchen"}, "movement"),
            1: event.Event("leave", {"location": "Kitchen"}, "movement"),
            2: event.Event("enter", {"location": "Living Room"}, "movement")
        }
    )

    alice = person.Person(
        "Alice Smith",
        25,
        events={
            0: event.Event("enter", {"location": "Kitchen"}, "movement"),
            2: event.Event("die", {"location": "Kitchen", "cause": "unknown"}, "status")
        }
    )

    jeff = person.Person(
        "Jeff Stein",
        40,
        events={
            0: event.Event("enter", {"location": "Kitchen"}, "movement"),
            3: event.Event("leave", {"location": "Kitchen"}, "movement")
        }
    )
    
    return john, alice, jeff
   
def sherlock_holmes(people, time, crimescene="Kitchen"):
    for person in people:
        location = person.get_location(time)
        print(f"{person.get_name()} is at {location} at time {time}.")


if __name__ == "__main__":
    john, alice, jeff = main()
    sherlock_holmes([john, alice, jeff], 1)
    sherlock_holmes([john, alice, jeff], 2)
    sherlock_holmes([john, alice, jeff], 3)
