#ifndef TAPAS_MAIN_H_
#define TAPAS_MAIN_H_

#include "tapas/common.h"

namespace tapas {

template <class BT, int POS_OFFSET>
class BodyInfo {
  public:
    typedef BT type;
    static const int pos_offset = POS_OFFSET;
};

// Generic Definition of the main class of Tapas framework
template <int DIM, class FP, class BT,
          class BT_ATTR, class CELL_ATTR,
          class PartitionAlgorithm>
class Tapas {
    // Generic definition of Tapas class.
    // This is just a placeholder and actual definition is provided by
    // partitioning algorithm plugins using template specialization.
};

} // namespace tapas


#endif // TAPAS_MAIN_H_ 
