#ifndef OPENMM_IC_DRUDE_LANGEVIN_INTEGRATOR_PROXY_H_
#define OPENMM_IC_DRUDE_LANGEVIN_INTEGRATOR_PROXY_H_

#include "internal/windowsExportIC.h"
#include "openmm/serialization/SerializationProxy.h"

namespace OpenMM {

class OPENMM_EXPORT_IC ICDrudeLangevinIntegratorProxy
    : public SerializationProxy {
   public:
    ICDrudeLangevinIntegratorProxy();
    void serialize(const void* object, SerializationNode& node) const;
    void* deserialize(const SerializationNode& node) const;
};

}  // namespace OpenMM

#endif /*OPENMM_IC_DRUDE_LANGEVIN_INTEGRATOR_PROXY_H_*/