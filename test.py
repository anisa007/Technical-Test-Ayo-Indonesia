import unittest

class TestBookingValidation(unittest.TestCase):
    # test case periksa harga 
    def test_price_validation(self):
        # Simulasi pengambilan data dari database menggunakan list
        stored_bookings = [ # Pemesanan yang tersimpan
            {"Booking_id": "BK/000001", "venue_id" : "15" ,"user_id" : "12","date": "2022-12-10", "Start_time": "09:00:00", "end_time": "11:00:00", "price": 1200000},
            {"Booking_id": "BK/000005", "venue_id" : "15", "user_id" : "12" ,"date": "2022-12-10", "Start_time": "09:00:00", "end_time": "11:00:00", "price": 1000000}
        ]
        # Harga yang seharusnya
        correct_prices = [
            {"id" :"11", "venue_id" : "15" , "date": "2022-12-10", "start_time": "07:00:00", "end_time": "09:00:00", "price": 800000},
            {"id" :"12", "venue_id" : "15" , "date": "2022-12-10", "start_time": "09:00:00", "end_time": "11:00:00", "price": 1000000},
            {"id" :"13", "venue_id" : "15" , "date": "2022-12-10", "start_time": "09:00:00", "end_time": "13:00:00", "price": 1200000}
        ]
        #check harga yang seharusnya
        for check_booking in stored_bookings:
            for check_correct_price in correct_prices:
                if (check_booking["venue_id"] == check_correct_price["venue_id"] and
                    check_booking["date"] == check_correct_price["date"] and
                    check_booking["Start_time"] == check_correct_price["start_time"] and
                    check_booking["end_time"] == check_correct_price["end_time"] and
                    check_booking["price"] != check_correct_price["price"]):
                    self.assertEqual(check_booking["price"], check_correct_price["price"], "Harga tidak sesuai dengan harga yang seharusnya")
    
    # test case periksa double booking 
    def test_double_booking_detection(self):
        # Simulasi pengambilan data dari database menggunakan list
        stored_bookings = [ # pemesanan yang tersimpan
           {"Booking_id": "BK/000001", "venue_id" : "15" ,"user_id" : "12","date": "2022-12-10", "Start_time": "09:00:00", "end_time": "11:00:00", "price": 1200000},
           {"Booking_id": "BK/000005", "venue_id" : "15", "user_id" : "12" ,"date": "2022-12-10", "Start_time": "09:00:00", "end_time": "11:00:00", "price": 1000000}
        ]
        # Check double booking
        for booking1 in (stored_bookings): 
            for booking2 in (stored_bookings): 
                if booking1 != booking2:
                    if (booking1["venue_id"] == booking2["venue_id"] and 
                        booking1["user_id"] == booking2["user_id"] and 
                        booking1["date"] == booking2["date"] and
                        booking1["Start_time"] == booking2["Start_time"] and
                        booking1["end_time"] == booking2["end_time"]):
                        self.fail(f"Double booking terdeteksi pada: {booking1['Booking_id']} and {booking2['Booking_id']}")


if __name__ == '__main__':
    unittest.main()
