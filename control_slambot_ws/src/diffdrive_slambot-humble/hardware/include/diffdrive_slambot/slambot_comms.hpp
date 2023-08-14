#ifndef DIFFDRIVE_slambot_slambot_COMMS_HPP
#define DIFFDRIVE_slambot_slambot_COMMS_HPP
#include <iostream>


class slambotComms
{

public:

  slambotComms() = default;

  void connect(int32_t timeout_ms)
  {  
    timeout_ms_ = timeout_ms;
  
  }

  void disconnect()
  {

  }

  bool connected() const
  {
    return 1;
  }


  void send_empty_msg()
  {
  }

  void read_encoder_values(int &val_1, int &val_2)
  {
    

    std::string delimiter = " ";
    
  }
  void set_motor_values(int val_1, int val_2)
  {

  }

  void set_pid_values(int k_p, int k_d, int k_i, int k_o)
  {
  }

private:
    int timeout_ms_;
};

#endif // DIFFDRIVE_slambot_slambot_COMMS_HPP